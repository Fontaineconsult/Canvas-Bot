
from network.canvas_session_manager import CanvasSession
from bs4 import BeautifulSoup
from config.read import read_config
from core_canvas_classes.node_sorter import create_child_nodes
from core_canvas_classes.manifest import Manifest
from colorama import Fore, Style

wait_timers = read_config()['waits']
filters = read_config()['filters']
items_to_remove = read_config()['sorters']
titles = read_config()['titles']

class PageNode(object):

    def __init__(self, session: CanvasSession,
                 url: str,
                 root,
                 parent,
                 page_manifest: Manifest,
                 content_manifest: Manifest,
                 junk_manifest: list,
                 **kwargs):

        self.root = root
        self.root_node = False
        self.title = None
        self.parent = parent
        self.children = list()
        self.session = session
        self.url = url
        self.node_init_failed = False
        self.kwargs = kwargs
        self.scraper = filters[self.__class__.__name__]
        self.page_html = BeautifulSoup
        self.page_manifest = page_manifest
        self.content_manifest = content_manifest
        self.junk_manifest = junk_manifest
        self.node_links = list()
        self.create_child_nodes = lambda: create_child_nodes(self, **self.kwargs)
        self._init_node()

    def __str__(self):
        if self.node_init_failed:
            failed = f"{Fore.RED}Failed{Fore.LIGHTYELLOW_EX}"
        else:
            failed = "Success"
        return f"{Fore.LIGHTGREEN_EX}<{str(self.__class__.__name__)} {self.url} - {failed}>{Style.RESET_ALL}".strip()

    def _init_node(self):

        while not self.node_init_failed:

            if self.page_manifest.exists(self.url, self):
                self.node_init_failed = True

            if not self.node_init_failed:
                if "bypass_page_get" not in self.kwargs.keys():
                    self._get_page_html()

                self.page_manifest.add_item_to_manifest(self)
                self.root.tree_vis.add_node(self)

            if "bypass_sort" not in self.kwargs.keys():
                if not self.node_init_failed:
                    self._sort_links()
                    self.create_child_nodes()
            else:
                print("Bypassing sort for", self.url)

    def _get_page_html(self):
        if "requests_get" in self.kwargs.keys():
            print("ASDASDA")
            page_request = self.session.requests_get(self.url)
            print("REQUEST11111", page_request)
            if page_request:
                self.page_html = BeautifulSoup(page_request.content, "html.parser")
                self.get_title()
                print("REQUEST1", page_request)
                if isinstance(self.scraper, str):
                    self.page_html = self.page_html.find(self.scraper)
                else:
                    self.page_html = self.page_html.find(attrs=self.scraper)

            if not page_request or not self.page_html:

                print(f"{Fore.LIGHTYELLOW_EX}Request Filtering Failed, Switching to Selenium {self.url}{Style.RESET_ALL}")
                self.page_html = BeautifulSoup(self.session.selenium_get(self.url, wait_timers[self.__class__.__name__]), "html.parser")
                self.get_title()
                if isinstance(self.scraper, str):
                    self.page_html = self.page_html.find(self.scraper)
                else:
                    self.page_html = self.page_html.find(attrs=self.scraper)

            if self.page_html is None:
                print(f"{Fore.LIGHTRED_EX}No Page HTML {self.url}{Style.RESET_ALL}")
                self.node_init_failed = True
        else:
            print(self.url, "HERE")
            self.page_html = BeautifulSoup(self.session.selenium_get(self.url, wait_timers[self.__class__.__name__]), "html.parser")
            self.get_title()
            self.page_html = self.page_html.find(attrs=self.scraper)

            if self.page_html is None:
                print(f"{Fore.LIGHTRED_EX}No Page HTML {self.url}{Style.RESET_ALL}")
                self.node_init_failed = True

    def _sort_links(self):
        try:

            href_links_to_identify = list(set([a_tag.get('href') for a_tag in self.page_html.find_all('a')]))
            img_links_to_identify = list(set([a_tag.get('src') for a_tag in self.page_html.find_all('img')]))
            video_tag = list(set([a_tag.get('src') for a_tag in self.page_html.find_all('video')]))
            iframe_links_to_identify = list(set([src_tag.get('src') for src_tag in self.page_html.find_all('iframe')]))
            self.node_links = href_links_to_identify + iframe_links_to_identify + img_links_to_identify + video_tag
            self.node_links = [link for link in self.node_links if link not in items_to_remove['first-sort-remove']]

        except AttributeError as e:
            print(f"{Fore.LIGHTRED_EX}Sort Failed {self.url} - {e}{Style.RESET_ALL}")
            self.node_init_failed = True

    def find_link_parent(self, link: str):
        return self.page_html(href=link)

    def get_title(self):
        if not self.node_init_failed:
            get_title = self.page_html.find(titles[self.__class__.__name__])
            if get_title:
                self.title = get_title.text
            else:
                print(f"{Fore.LIGHTRED_EX}Can't find title with filter: {titles[self.__class__.__name__]} {self.url}{Style.RESET_ALL}")
                self.title = self.__class__.__name__




