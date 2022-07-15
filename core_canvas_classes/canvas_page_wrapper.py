from canvas_page_classes.announcements import Announcements
from canvas_page_classes.discussions import Discussions
from canvas_page_classes.home import Home
from canvas_page_classes.pages import Pages
from network.canvas_session_manager import CanvasSession
from canvas_page_classes.modules import Modules
from canvas_page_classes.assignments import Assignments
from dotenv import load_dotenv
from os.path import join, dirname
from core_canvas_classes.manifest import Manifest
from colorama import Fore, Style
import os
from tools.canvas_tree_viewer import CanvasTree

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class CanvasCourseWrapper:

    def __init__(self, course_id, scraper: CanvasSession, **kwargs):
        self.canvas_root_url = os.environ.get("canvas_course_page_root")
        self.canvas_course_id = course_id
        self.course_page_url = f"{self.canvas_root_url}/{self.canvas_course_id}"
        self.modules_page_root = None
        self.assignments_page_root = None
        self.pages_page_root = None
        self.announcements_page_root = None
        self.home_page_root = None
        self.discussions_page_root = None
        self.scraper = scraper
        self.kwargs = kwargs
        self.page_manifest = Manifest()
        self.content_manifest = Manifest()
        self.junk_manifest = list()
        self.canvas_module_tree_visualization = CanvasTree()

    def __str__(self):
        return f"<{Fore.GREEN}Canvas Course Root ID: {self.canvas_course_id}{Style.RESET_ALL}>"

    def _init_home_root(self):
        home_page = self.scraper.requests_get(f"{self.course_page_url}/pages/homepage")
        if home_page.ok:
            self.home_page_root = Home(self.scraper,
                                       f"{self.course_page_url}/pages/homepage",
                                       self.canvas_module_tree_visualization,
                                       self,
                                       self.page_manifest,
                                       self.content_manifest,
                                       self.junk_manifest,
                                       **self.kwargs)

    def _init_modules_root(self):
        self.modules_page_root = Modules(self.scraper,
                                         f"{self.course_page_url}/modules",
                                         self.canvas_module_tree_visualization,
                                         self,
                                         self.page_manifest,
                                         self.content_manifest,
                                         self.junk_manifest,
                                         **self.kwargs)

    def _init_assignments_root(self):
        self.assignments_page_root = Assignments(self.scraper,
                                             f"{self.course_page_url}/assignments",
                                             self.canvas_module_tree_visualization,
                                             self,
                                             self.page_manifest,
                                             self.content_manifest,
                                             self.junk_manifest,
                                             **self.kwargs)

    def _init_pages_root(self):
        self.pages_page_root = Pages(self.scraper,
                                       f"{self.course_page_url}/pages",
                                       self.canvas_module_tree_visualization,
                                       self,
                                       self.page_manifest,
                                       self.content_manifest,
                                       self.junk_manifest,
                                       **self.kwargs)


    def _init_announcements_root(self):
        self.announcements_page_root = Announcements(self.scraper,
                                       f"{self.course_page_url}/announcements",
                                       self.canvas_module_tree_visualization,
                                       self,
                                       self.page_manifest,
                                       self.content_manifest,
                                       self.junk_manifest,
                                       **self.kwargs)


    def _init_discussions_root(self):
        self.discussions_page_root = Discussions(self.scraper,
                                                     f"{self.course_page_url}/discussion_topics",
                                                     self.canvas_module_tree_visualization,
                                                     self,
                                                     self.page_manifest,
                                                     self.content_manifest,
                                                     self.junk_manifest,
                                                     **self.kwargs)


    def initialize(self):
        self.canvas_module_tree_visualization.init_node(self)

        if not self.kwargs.get("ignore_home") is True:
            self._init_home_root()
        if not self.kwargs.get("ignore_modules") is True:
            self._init_modules_root()
        if not self.kwargs.get("ignore_assignments") is True:
            self._init_assignments_root()
        if not self.kwargs.get("ignore_pages") is True:
            self._init_pages_root()
        if not self.kwargs.get("ignore_announcements") is True:
            self._init_announcements_root()
        if not self.kwargs.get("ignore_discussions") is True:
            self._init_discussions_root()
    def add_node_to_tree_vis(self, node):
        self.canvas_module_tree_visualization.add_node(node)

    def view_canvas_tree(self):
        return self.canvas_module_tree_visualization.show_nodes()


