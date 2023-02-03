from colorama import Fore, Style

from canvas_page_classes.page import Page
from core_canvas_classes.generic_page_node import PageNode
from config.read import read_config

filters = read_config()['filters']

class Pages(PageNode):

    def __init__(self, session, url, tree_vis, parent, page_manifest, content_manifest, junk_manifest, **kwargs):
        self.kwargs = kwargs
        self.tree_vis = tree_vis
        PageNode.__init__(self, session, url, self, parent,
                          page_manifest, content_manifest,
                          junk_manifest,
                          bypass_sort=True,
                          **kwargs)
        self._build_modules()

    def __str__(self):
        if self.node_init_failed:
            failed = f"{Fore.RED}Failed{Fore.LIGHTYELLOW_EX}"
        else:
            failed = "Success"
        return f"{Fore.LIGHTYELLOW_EX}<{str(self.__class__.__name__)} {self.url} - {failed}>{Style.RESET_ALL}"

    def _build_modules(self):
        self.kwargs.pop("bypass_sort")
        pages = self.page_html.find_all(attrs=filters['PagesLinks'])
        for each_page in pages:
            if each_page['href']:
                self.children.append(Page(self.session,
                                            each_page['href'],
                                            self,
                                            self,
                                            self.page_manifest,
                                            self.content_manifest,
                                            self.junk_manifest,
                                            bypass_sort=False,
                                            **self.kwargs))