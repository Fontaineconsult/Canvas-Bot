from canvas_session_manager import CanvasSession

session = CanvasSession()
session.init()


def download_file(uri: str, session: CanvasSession):

    file = session.requests_get(uri)
    print(file.content)


download_file('https://sfsu.instructure.com/courses/6209/files/700927/download', session)