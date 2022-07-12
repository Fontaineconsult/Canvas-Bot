from core_canvas_classes.generic_page_node import PageNode
from bs4 import BeautifulSoup
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

    # def _get_page_html(self):
    #     raw_request = self.session.requests_get(self.url)
    #     if raw_request:
    #         if raw_request.ok:
    #             try:
    #                 self.title = BeautifulSoup(raw_request.content, "html.parser").find("title").text
    #             except AttributeError:
    #                 print(f"{Fore.LIGHTRED_EX}No Title Tag {self.url}{Style.RESET_ALL}")
    #
    #
    #             self.page_html = BeautifulSoup(raw_request.content, "html.parser").find('body')
    #             if self.page_html is None:
    #                 print(f"{Fore.LIGHTRED_EX}Can't Find Body Tag in {self.url}{Style.RESET_ALL}")
    #
    #         if raw_request.status_code == 404:
    #             print(f"{Fore.LIGHTRED_EX}External Page is unreachable {self.url}{Style.RESET_ALL}")
    #             self.node_init_failed = True
    #
    #     else:
    #         print(f"{Fore.LIGHTRED_EX}Node Init Failed {self.url}{Style.RESET_ALL}")
    #         self.node_init_failed = True

