
from network.canvas_session_manager import CanvasSession
from sorters.resource_identifier import canvas_resource_identifier
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from core_canvas_classes.node_sorter import create_child_nodes
from os.path import join, dirname
from config.read import read_config
from colorama import Fore, Style

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
titles = read_config()['titles']
items_to_remove = read_config()['sorters']


class PageComponentNode:

    def __init__(self, session: CanvasSession,
                 component_div: BeautifulSoup,
                 root,
                 parent,
                 page_manifest: dict,
                 content_manifest: dict,
                 junk_manifest: list,
                 count: int,
                 **kwargs):

        self.root = root
        self.parent = parent
        self.children = list()
        self.session = session
        self.url = self.parent.url
        self.page_html = component_div
        self.page_manifest = page_manifest
        self.count = count
        self.kwargs = kwargs
        self.content_manifest = content_manifest
        self.junk_manifest = junk_manifest
        self.title = None
        self.node_links = list()

        self.create_child_nodes = lambda: create_child_nodes(self, **self.kwargs)
        self._init_node()

    def __str__(self):
        return f"{Fore.MAGENTA}<{self.__class__.__name__}-{self.count} - {self.title}>{Style.RESET_ALL}".replace(" ", "")

    def _init_node(self):
        self.get_component_title()
        self._sort_links()
        self.root.tree_vis.add_node(self)
        self.create_child_nodes()


    def get_component_title(self):
        self.title = self.page_html.find(titles[self.__class__.__name__]).text


    def _sort_links(self):

        href_links_to_identify = list(set([a_tag.get('href') for a_tag in self.page_html.find_all('a')]))
        img_links_to_identify = list(set([a_tag.get('src') for a_tag in self.page_html.find_all('img')]))
        iframe_links_to_identify = list(set([src_tag.get('src') for src_tag in self.page_html.find_all('iframe')]))
        self.node_links = href_links_to_identify + iframe_links_to_identify + img_links_to_identify
        self.node_links = [link for link in self.node_links if link not in items_to_remove['first-sort-remove']]

        # self.node_links = list(set([a_tag.get('href') for a_tag in self.component_div.find_all('a') if isinstance(a_tag.get('href'), str)]))

    def find_link_parent(self, link):
        return self.page_html(href=link)







