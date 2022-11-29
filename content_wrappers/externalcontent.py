from bs4 import BeautifulSoup

from content_wrappers.content import Content
from core_canvas_classes.generic_page_node import PageNode
from network.canvas_session_manager import CanvasSession


class WebDocumentApplication(Content):
    ## not using

    def __init__(self, link: str, local_session: CanvasSession, parent: PageNode, root):
        Content.__init__(self, link, local_session, parent, root)
        self.downloadable = False
        self.is_document = True
        self.is_image = False
        self.is_audio = False
        self.is_video = False
        self.find_title()

    def find_title(self):
        self.session.requests_get(self.url)
        self.title = BeautifulSoup(self.session.requests_get(self.url).content, "html.parser").find('title').text
