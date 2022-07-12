from colorama import Fore, Style

from canvas_page_classes.page import Page
from core_canvas_classes.generic_page_component_node import PageComponentNode
from core_canvas_classes.generic_page_node import PageNode
from config.read import read_config

filters = read_config()['filters']

class Home(PageNode):

    def __init__(self, session, url, tree_vis, parent, page_manifest, content_manifest, junk_manifest, **kwargs):
        self.kwargs = kwargs
        self.tree_vis = tree_vis
        PageNode.__init__(self, session, url, self, parent,
                          page_manifest, content_manifest,
                          junk_manifest,
                          **kwargs)


    def __str__(self):
        if self.node_init_failed:
            failed = f"{Fore.RED}Failed{Fore.LIGHTYELLOW_EX}"
        else:
            failed = "Success"
        return f"{Fore.LIGHTYELLOW_EX}<{str(self.__class__.__name__)} {self.url} - {failed}>{Style.RESET_ALL}"