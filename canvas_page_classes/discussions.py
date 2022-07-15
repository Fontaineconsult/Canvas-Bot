from colorama import Fore, Style

from canvas_page_classes.assignments_group import AssignmentsGroup
from canvas_page_classes.discussions_group import DiscussionsGroup
from core_canvas_classes.generic_page_node import PageNode
from urllib.parse import urljoin, urlparse

from config.read import read_config

filters = read_config()['filters']


class Discussions(PageNode):



    def __init__(self, session, url, tree_vis, parent, page_manifest, content_manifest, junk_manifest: list, **kwargs):
        self.cleaned_url = urljoin(url, urlparse(url).path)
        self.tree_vis = tree_vis
        PageNode.__init__(self, session,
                          self.cleaned_url, self,
                          parent, page_manifest,
                          content_manifest, junk_manifest,
                          bypass_sort=True, **kwargs)
        self._build_discussions()
        self.kwargs = kwargs

    def __str__(self):
        if self.node_init_failed:
            failed = f"{Fore.RED}Failed{Fore.LIGHTYELLOW_EX}"
        else:
            failed = "Success"
        return f"{Fore.LIGHTYELLOW_EX}<{str(self.__class__.__name__)} {self.url} - {failed}>{Style.RESET_ALL}"

    def _build_discussions(self):

        context_modules = self.page_html.find_all(attrs=filters['DiscussionsGroup'])
        for count, each_module in enumerate(context_modules):

            self.children.append(DiscussionsGroup(self.session,
                                                  each_module,
                                                  self,
                                                  self,
                                                  self.page_manifest,
                                                  self.content_manifest,
                                                  self.junk_manifest,
                                                  count,
                                                  **self.kwargs))