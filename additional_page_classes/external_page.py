from core_canvas_classes.generic_page_node import PageNode
from colorama import Fore, Style

class ExternalPage(PageNode):

    def __init__(self, session,
                 url, root, parent,
                 page_manifest: dict, content_manifest: dict,
                 junk_manifest: list, **kwargs):

        PageNode.__init__(self,
                          session,
                          url,
                          root,
                          parent,
                          page_manifest,
                          content_manifest,
                          junk_manifest,
                          bypass_external_nodes=True,
                          bypass_canvas_file_nodes=True,
                          requests_get=True,
                          **kwargs)

    def __str__(self):
        if self.node_init_failed:
            failed = f"{Fore.RED}Failed{Fore.LIGHTYELLOW_EX}"
        else:
            failed = "Success"
        return f"{Fore.LIGHTMAGENTA_EX}<{str(self.__class__.__name__)} {self.url} - {failed}>{Style.RESET_ALL}"

