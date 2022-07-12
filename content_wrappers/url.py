from content_wrappers.content import Content
from network.canvas_session_manager import CanvasSession
from core_canvas_classes.generic_page_node import PageNode



class ContentURL(Content):

    def __init__(self, link: str, local_session: CanvasSession, parent: PageNode, root):
        Content.__init__(self, link, local_session, parent, root)
        self.title_search()


    def title_search(self):
        a_tags = self.parent.find_link_parent(self.url)
        if a_tags:
            for a_tag in a_tags:
                children = a_tag.findChildren()
                for child in children:
                    if len(child.attrs.keys()) == 0:
                        if len(child.text) > 0 or child.text is not None:
                            self.title = child.text


class ContentURLVideo(Content):

    def __init__(self, link: str, local_session: CanvasSession, parent: PageNode, root):
        Content.__init__(self, link, local_session, parent, root)
        self.is_video = True
        self.title_search()


    def title_search(self):
        a_tags = self.parent.find_link_parent(self.url)
        if a_tags:
            for a_tag in a_tags:
                children = a_tag.findChildren()
                for child in children:
                    if len(child.attrs.keys()) == 0:
                        if len(child.text) > 0 or child.text is not None:
                            self.title = child.text


class ContentURLAudio(Content):

    def __init__(self, link: str, local_session: CanvasSession, parent: PageNode, root):
        Content.__init__(self, link, local_session, parent, root)
        self.is_audio = True
        self.title_search()


    def title_search(self):
        a_tags = self.parent.find_link_parent(self.url)
        if a_tags:
            for a_tag in a_tags:
                children = a_tag.findChildren()
                for child in children:
                    if len(child.attrs.keys()) == 0:
                        if len(child.text) > 0 or child.text is not None:
                            self.title = child.text