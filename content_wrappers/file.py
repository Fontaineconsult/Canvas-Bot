import warnings
from urllib.parse import urlparse, urlunsplit

from colorama import Fore, Style

from content_wrappers.content import Content
from network.canvas_session_manager import CanvasSession
from bs4 import BeautifulSoup

from sorters.sorter_re import mime_check_image, mime_check_document, mime_check_video, mime_check_audio
from sorters.sorting_tools import get_mime_type


class ContentFile(Content):

    def __init__(self, link: str, local_session: CanvasSession, parent, root):
        Content.__init__(self, link, local_session, parent, root)
        self.downloadable = True
        self.is_document = True



class ContentVideo(Content):
    def __init__(self, link: str, local_session: CanvasSession, parent, root):
        Content.__init__(self, link, local_session, parent, root)
        self.downloadable = True
        self.is_video = True



class ContentAudio(Content):
    def __init__(self, link: str, local_session: CanvasSession, parent, root):
        Content.__init__(self, link, local_session, parent, root)
        self.downloadable = True
        self.is_audio = True
        self.mime_type = get_mime_type(link)


class ContentImage(Content):
    def __init__(self, link: str, local_session: CanvasSession, parent, root):
        self.alt_tag = None
        Content.__init__(self, link, local_session, parent, root)
        self.downloadable = True
        self.is_image = True


    def __str__(self):

        if self.alt_tag:
            return f"( {self.__class__.__name__} - {self.url} ALT:TRUE)"
        else:
            return f"( {self.__class__.__name__} - {self.url} ALT:FALSE)"

    def find_alt_tag(self):

        parent_tag = self.parent.page_html(src=self.url)
        if len(parent_tag) > 0:
            if "alt" in parent_tag[0].attrs:
                self.alt_tag = parent_tag[0].attrs['alt']
        return self.alt_tag


class ContentDocument(Content):
    def __init__(self, link: str, local_session: CanvasSession, parent, root):
        Content.__init__(self, link, local_session, parent, root)
        self.downloadable = True
        self.is_document = True



class ContentUserCanvasFile(Content):
    def __init__(self, link: str, local_session: CanvasSession, parent, root):
        self.alt_tag = None
        Content.__init__(self, link, local_session, parent, root)
        self.downloadable = True
        self.get_data_from_header()
        self.mime_type = None


    def get_data_from_header(self):
        self.header = self.session.requests_header(self.url).headers

        if self.header['Status'] == '302 Found':
            self.resource_location = self.header['location']
            self.mime_type = get_mime_type(self.resource_location)
        else:
            print(f"{Fore.LIGHTRED_EX}No Download Location found for {self.url} | {self.header['status']}{Style.RESET_ALL}")


    def find_alt_tag(self):

        parent_tag = self.parent.page_html(src=self.url)
        if len(parent_tag) > 0:
            if "alt" in parent_tag[0].attrs:
                self.alt_tag = parent_tag[0].attrs['alt']
        return self.alt_tag


class ContentCanvasFile(Content):

    def __init__(self, link: str, local_session: CanvasSession, parent, root):
        self.session = local_session
        self.url = link
        self.page_html = None
        self.alt_tag = None
        self._get_page_html()
        self.title = self.find_title()
        self.resource_location = self.check_resource_location()
        self.mime_type = None
        self.get_data_from_header()
        self.header = None
        Content.__init__(self, self.url, local_session, parent, root, self.title, self.mime_type, self.resource_location)
        self.set_documement_type()




    def __str__(self):
        return f"( {self.__class__.__name__} - {self.check_resource_location()} - {self.title} )>"

    def _get_page_html(self):
        parse_url = urlparse(self.url)

        if parse_url.path.split("/")[-1] in ["download", "preview"]:
            remove_end = parse_url.path.split("/")[0:-1]
            unsplit = urlunsplit((parse_url.scheme, parse_url.netloc,
                                  "/".join(remove_end),
                                    "",""))
            self.url = unsplit
            page_request = self.session.requests_get(self.url)


        else:
            page_request = self.session.requests_get(self.url)

        if page_request:
            self.page_html = page_request.content

    def check_resource_location(self):
        print("BEFORE PARSE", self.url)
        parse_url = urlparse(self.url)

        if parse_url.path.split("/")[-1] in ["download", "preview"]:


            remove_end = parse_url.path.split("/")[0:-1]
            remove_end.append("download")
            add_download = "/".join(remove_end)
            return urlunsplit((parse_url.scheme, parse_url.netloc,
                               add_download,
                                "",""))

        else:
            split_path = parse_url.path.split("/")
            split_path.append("download")
            add_download = "/".join(split_path)
            return urlunsplit((parse_url.scheme, parse_url.netloc,
                           add_download,"",""))

    def get_data_from_header(self, location_url=None):
        print("AFTER PARSE", self.resource_location)
        if location_url:
            header_url = location_url
            header_request = self.session.requests_header(header_url)
            print("from location", header_request.status_code, header_request.headers)

        else:
            header_url = self.check_resource_location()
            header_request = self.session.requests_header(header_url)
            print("from resource location", header_request.status_code, header_request.headers)
        if header_request:
            self.header = header_request.headers
            if header_request.status_code == 200:
                self.mime_type = self.header['Content-Type']
            elif header_request.status_code == 302:
                self.get_data_from_header(self.header['location'])
            else:
                print(f"{Fore.LIGHTRED_EX}Could not locate MimeType {header_url}{Style.RESET_ALL}")
                print(self.header)

    def set_documement_type(self):
        if self.mime_type is None:
            self.get_data_from_header(self.resource_location)

        try:
            if mime_check_image.search(self.mime_type):
                self.is_image = True

            if mime_check_document.search(self.mime_type):
                self.is_document = True

            if mime_check_video.search(self.mime_type):
                self.is_video = True

            if mime_check_audio.search(self.mime_type):
                self.is_audio = True
        except TypeError:
            warnings.warn("No MimeType specified can't set content type")
            print(self.header)
            print(self.resource_location)

    def find_alt_tag(self):
        pass


    def find_title(self):

        try:
            return BeautifulSoup(self.page_html, "html.parser").find('h2').text

        except (AttributeError, TypeError):
            print("No H2 tag found in CanvasFile page", self.url)
            return "No Title Found"
