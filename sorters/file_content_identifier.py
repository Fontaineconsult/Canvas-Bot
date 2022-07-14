import re
from typing import Optional
from urllib.parse import urlparse, quote

from content_wrappers.file import ContentDocument, ContentCanvasFile, ContentVideo, ContentAudio, ContentImage, \
    ContentUserCanvasFile
from network.canvas_session_manager import CanvasSession
from dotenv import load_dotenv
import os
from os.path import join, dirname

from sorters.sorting_tools import is_url_valid

from sorters.sorter_re import canvas_file_content_regex, document_content_regex, video_file_resources, \
    audio_file_resources, image_content_regex, canvas_user_file_content_regex

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
instructure_root = os.environ.get("canvas_course_page_root")


def create_full_url(resource, parent_url):

    sep = "/"
    parsed_parent_url = urlparse(parent_url)
    netloc = parsed_parent_url.netloc
    url = sep.join(parsed_parent_url.path.split("/")[0:-1])
    url = quote(url + f"/{resource}")
    return parsed_parent_url.scheme + "://" + netloc + url

def document_file_identifier(link: str, local_session: CanvasSession, parent, root) -> Optional[ContentDocument]:

    if link is None:
        return None

    if "allow_incomplete_url_sort" not in parent.kwargs.keys():
        if not is_url_valid(link):
            link = create_full_url(link, parent.url)

    match_link = document_content_regex.match(link)
    if bool(match_link):

        return ContentDocument(match_link.group(), local_session, parent, root)
    else:
        return None


def video_file_identifier(link: str, local_session: CanvasSession, parent, root) -> Optional[ContentVideo]:

    if link is None:
        return None

    if "allow_incomplete_url_sort" not in parent.kwargs.keys():
        if not is_url_valid(link):
            link = create_full_url(link, parent.url)

    match_link = video_file_resources.match(link)

    if bool(match_link):

        return ContentVideo(match_link.group(), local_session, parent, root)
    else:
        return None


def audio_file_identifier(link: str, local_session: CanvasSession, parent, root) -> Optional[ContentAudio]:

    if link is None:
        return None

    if "allow_incomplete_url_sort" not in parent.kwargs.keys():
        if not is_url_valid(link):
            link = create_full_url(link, parent.url)

    match_link = audio_file_resources.match(link)

    if bool(match_link):

        return ContentAudio(match_link.group(), local_session, parent, root)
    else:
        return None



def image_file_identifier(link: str, local_session: CanvasSession, parent, root) -> Optional[ContentImage]:

    if link is None:
        return None

    if "allow_incomplete_url_sort" not in parent.kwargs.keys():
        if not is_url_valid(link):
            link = create_full_url(link, parent.url)

    match_link = image_content_regex.match(link)

    if bool(match_link):


        return ContentImage(match_link.group(), local_session, parent, root)
    else:
        return None



def canvas_file_indentifier(link: str, local_session: CanvasSession, parent, root) -> Optional[ContentCanvasFile]:

    if link is None:
        return None



    match_link = canvas_file_content_regex.match(link)
    if bool(match_link):
        return ContentCanvasFile(match_link.group(), local_session, parent, root)

    return None



def canvas_user_file_identifer(link: str, local_session: CanvasSession, parent, root) -> Optional[ContentUserCanvasFile]:

    if link is None:
        return None

    match_link = canvas_user_file_content_regex.match(link)
    if bool(match_link):
        return ContentUserCanvasFile(match_link.group(), local_session, parent, root)

    return None