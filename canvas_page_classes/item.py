from core_canvas_classes.generic_page_node import PageNode
from bs4 import BeautifulSoup

class Item(PageNode):

    def __init__(self, session, url, root, parent, page_manifest, content_manifest, junk_manifest: list, **kwargs):
        PageNode.__init__(self, session, url, root, parent, page_manifest, content_manifest, junk_manifest, **kwargs)

    # def _get_page_html(self):
    #     self.page_html = BeautifulSoup(self.session.selenium_get(self.url, 1), "html.parser").find("div", self.scraper)
