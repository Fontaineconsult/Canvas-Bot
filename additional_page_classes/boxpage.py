import json

from colorama import Fore, Style
from bs4 import BeautifulSoup
import re
from core_canvas_classes.generic_page_node import PageNode
from core_canvas_classes.node_sorter import create_child_nodes
from config.read import read_config

filters = read_config()['filters']

class BoxPage(PageNode):

    def __init__(self, session, url, tree_vis,
                 parent, page_manifest,
                 content_manifest,
                 junk_manifest: list,
                 **kwargs):

        self.tree_vis = tree_vis
        PageNode.__init__(self, session, url, self.tree_vis, parent,
                          page_manifest,
                          content_manifest,
                          junk_manifest,
                          requests_get=True,
                          bypass_sort=True,
                          allow_incomplete_url_sort=True,
                          )
        self.kwargs = kwargs
        self._build_content_children()

    def __str__(self):
        if self.node_init_failed:
            failed = f"{Fore.RED}Failed{Fore.LIGHTCYAN_EX}"
        else:
            failed = "Success"
        return f"{Fore.LIGHTCYAN_EX}<{str(self.__class__.__name__)} {self.url} - {failed}>{Style.RESET_ALL}"


    def _build_content_children(self):

        page_request = self.session.requests_get(self.url)
        if page_request:
            self.page_html = BeautifulSoup(page_request.content, features="lxml")

            page_scripts = self.page_html.find_all(filters[self.__class__.__name__])
            expression = re.compile("Box\.postStreamData")
            items_expression = re.compile('"items":\[\{.*.}]')

            for script in page_scripts:
                if expression.search(script.text):

                    clean_text = script.text.replace("'","")

                    items = items_expression.search(clean_text)

                    raw_string_dict = f"{{{items.group()}}}"

                    try:
                        json_dict = json.loads(raw_string_dict)

                    except json.decoder.JSONDecodeError:
                        raw_string_dict = raw_string_dict + "}"
                        json_dict = json.loads(raw_string_dict)

                    for item in json_dict['items']:

                        self.node_links.append(item['name'])
            self.kwargs.update(allow_incomplete_url_sort=True)
            create_child_nodes(self, **self.kwargs)
        else:
            self.node_init_failed = True

