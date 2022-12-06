from network.canvas_session_manager import CanvasSession
from core_canvas_classes.content_extractor import ContentExtractor

class CanvasBot:


    def __init__(self, course_id, **kwargs):
        self.course_id = course_id
        self.kwargs = kwargs
        self.CanvasSession = CanvasSession()
        self.Content = ContentExtractor


    def start(self):
        self.CanvasSession.init()
        self.Content = ContentExtractor(self.course_id, self.CanvasSession, **self.kwargs)
        self.Content.initialize()
        self.Content.view_canvas_tree()
        self.CanvasSession.SeleniumSession.driver.close()

    def print_content_manifest(self):

        self.Content.content_manifest.print_manifest()
