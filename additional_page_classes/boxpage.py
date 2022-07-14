import json

from colorama import Fore, Style
from bs4 import BeautifulSoup
import re
from content_wrappers.content import Content
from core_canvas_classes.generic_page_node import PageNode
from core_canvas_classes.manifest import Manifest
from network.canvas_session_manager import CanvasSession
from config.read import read_config

filters = read_config()['filters']

class BoxPage(PageNode):

    def __init__(self, session, url, tree_vis,
                 parent, page_manifest, content_manifest, junk_manifest: list, **kwargs):
        self.tree_vis = tree_vis

        PageNode.__init__(self, session, url, self.tree_vis, parent,
                          page_manifest,
                          content_manifest,
                          junk_manifest,
                          bypass_page_get=True,
                          requests_get=True,
                          bypass_sort=True,
                          **kwargs)
        self.kwargs = kwargs
        self._build_content_children()

    def __str__(self):
        if self.node_init_failed:
            failed = f"{Fore.RED}Failed{Fore.LIGHTCYAN_EX}"
        else:
            failed = "Success"
        return f"{Fore.LIGHTCYAN_EX}<{str(self.__class__.__name__)} {self.url} - {failed}>{Style.RESET_ALL}"


    def _build_content_children(self):
        self.page_html = self.session.requests_get(self.url).content
        page_scripts = BeautifulSoup(self.page_html).find_all(filters[self.__class__.__name__])
        expression = re.compile("Box\.postStreamData")
        items_expression = re.compile('"items":\[\{.*.}]')

        for script in page_scripts:
            if expression.search(script.text):

                clean_text = script.text.replace("'","")

                items = items_expression.search(clean_text)

                raw_string_dict = f"{{{items.group()}}}"
                print(raw_string_dict)
                json_dict = json.loads(raw_string_dict)
                print(json_dict)



