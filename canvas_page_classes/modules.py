from colorama import Fore, Style

from core_canvas_classes.generic_page_node import PageNode
from canvas_page_classes.module import Module
from config.read import read_config

filters = read_config()['filters']


class Modules(PageNode):

    def __init__(self, session, url, tree_vis,
                 parent, page_manifest, content_manifest, junk_manifest: list, **kwargs):
        self.tree_vis = tree_vis
        PageNode.__init__(self, session, url, self, parent,
                          page_manifest, content_manifest, junk_manifest, bypass_sort=True, **kwargs)
        self.kwargs = kwargs
        self._build_modules()

    def __str__(self):
        if self.node_init_failed:
            failed = f"{Fore.RED}Failed{Fore.LIGHTYELLOW_EX}"
        else:
            failed = "Success"
        return f"{Fore.LIGHTYELLOW_EX}<{str(self.__class__.__name__)} {self.url} - {failed}>{Style.RESET_ALL}"


    def _build_modules(self):

        context_modules = self.page_html.find_all(attrs=filters['Module'])

        for count, each_module in enumerate(context_modules):

            module_id = each_module.select('div', attrs={"class": "item-group-condensed"})[0].get('id')
            self.children.append(Module(self.session,
                                        each_module,
                                        self,
                                        self,
                                        self.page_manifest,
                                        self.content_manifest,
                                        self.junk_manifest,
                                        count,
                                        module_id,
                                        bypass_sort=False,
                                        **self.kwargs))

