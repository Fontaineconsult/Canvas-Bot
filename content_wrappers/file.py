import mimetypes
from urllib.parse import urljoin, urlparse

from colorama import Fore, Style

from content_wrappers.content import Content
from network.canvas_session_manager import CanvasSession
from bs4 import BeautifulSoup

from sorters.sorter_re import mime_check_image


def get_mime_type(link):

    clean_url = urljoin(link, urlparse(link).path)
    mime_type = mimetypes.MimeTypes().guess_type(clean_url)[0]
    if mime_type is None:
        return 'text/plain'
    return mime_type


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
        self._get_page_html()
        self.title = None
        self.alt_tag = None
        self.find_title()
        Content.__init__(self, link, local_session, parent, root, self.title)

        self.page_html = None
        self.is_document = True
        self.resource_location = "{}/{}".format(link, "download")
        self.get_data_from_header()
        self.set_documement_type()

    def __str__(self):
        return f"( {self.__class__.__name__} - {self.url} - {self.title} )>"

    def _get_page_html(self):
        page_request = self.session.requests_get(self.url)
        if page_request:
            self.page_html = page_request.content
        else:
            self.downloadable = False


    def get_data_from_header(self):
        self.header = self.session.requests_header(self.url)
        print(self.url)
        print(self.header)
        if self.header:
            self.header = self.header.headers
            print(self.header['Status'])
            if self.header['Status'] == '200 Ok':
                print(self.header)
                self.mime_type = get_mime_type(self.header['Content-Type'])
                self.title = self.header['Content-Disposition']
            if self.header['Status'] == '302 Found':

                self.mime_type = get_mime_type(self.header['location'])
            else:
                print(f"{Fore.LIGHTRED_EX}No Download Location found for {self.url}{Style.RESET_ALL}")

    def set_documement_type(self):

        if mime_check_image.search(self.mime_type):
            self.is_document = False
            self.is_image = True

    def find_alt_tag(self):
        pass


    def find_title(self):
        self.downloadable = True
        if self.downloadable:
            try:
                self.title = BeautifulSoup(self.page_html, "html.parser").find('h2').text
            except AttributeError:
                print("No H2 tag found in CanvasFile page", self.url)


