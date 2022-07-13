from colorama import Fore, Style

from content_wrappers.content import Content
from core_canvas_classes.generic_page_node import PageNode
from core_canvas_classes.manifest import Manifest
from network.canvas_session_manager import CanvasSession


class BoxFile(Content):

    def __init__(self, link: str, local_session: CanvasSession, parent, root):
        Content.__init__(self, link, local_session, parent, root)

    def __str__(self):
        return f"( {self.__class__.__name__} - {self.url} - {self.title} - {self.order} )"
