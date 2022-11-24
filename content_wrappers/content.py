import mimetypes
from urllib.parse import urljoin, urlparse

from network.canvas_session_manager import CanvasSession
from core_canvas_classes.generic_page_node import PageNode


def get_mime_type(link):

    clean_url = urljoin(link, urlparse(link).path)
    mime_type = mimetypes.MimeTypes().guess_type(clean_url)[0]
    if mime_type is None:
        return 'text/plain'
    return mime_type



class Content:



    def __init__(self, link: str, local_session: CanvasSession, parent: PageNode, root, title=None):
        self.parent = parent
        self.root = root
        self.session = local_session
        self.url = link
        self.resource_location = None
        self.title = title
        self.is_video = False
        self.is_audio = False
        self.is_document = False
        self.is_image = False
        self.tail = True
        self.root_node = False
        self.downloadable = False
        self.is_hidden = False
        self.pseudo_content = False
        self.order = 0
        self.children = list()
        self.mime_type = get_mime_type(link)
        self._init_node()

    def __str__(self):
        return f"( {self.__class__.__name__} - {self.url} - {self.title} - {self.order} )"

    def _init_node(self):
        self.get_order()
        self.root.tree_vis.add_node(self)



    def get_order(self):
        from core_canvas_classes.generic_page_component_node import PageComponentNode

        def recurse_up(node):
            if isinstance(node, PageComponentNode):
                self.order = node.count
                return
            if node == self.root:
                return
            else:
                recurse_up(node.parent)

        recurse_up(self.parent)

    def download(self):
        if self.downloadable:
            return self.session.requests_get(self.url).content
        else:
            raise Warning(f"Content not downloadable: {self.url}")
