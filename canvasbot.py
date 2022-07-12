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




#
# for number in range(317,325):
#


Bot = CanvasBot("330")
Bot.start()
content = Bot.Content.all_content_to_json()





# documents = Bot.Content.get_documents()
# for each in documents:
#     print(each)

# image = Bot.Content.get_images()
# for each in image:
#     print(each)