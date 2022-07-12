from core_canvas_classes.generic_page_node import PageNode
from core_canvas_classes.manifest import Manifest
from urllib.parse import urljoin, urlparse

class Page(PageNode):

    def __init__(self, session, url, root, parent, page_manifest: Manifest, content_manifest: Manifest, junk_manifest: list,
                 **kwargs):
        self.cleaned_url = urljoin(url, urlparse(url).path)
        PageNode.__init__(self, session, self.cleaned_url,
                          root, parent, page_manifest,
                          content_manifest, junk_manifest,
                          **kwargs)

