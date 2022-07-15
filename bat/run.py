import os, sys

def run(course_id):
    bot = CanvasBot(course_id)
    bot.start()
    print(bot.Content.all_content_to_json())

if __name__ == '__main__':

    sys.path.append(r"C:\Users\913678186\IdeaProjects\Canvas-Bot")
    from canvasbot import CanvasBot
    run(int(sys.argv[1]))