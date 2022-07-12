import re
from typing import Optional

from content_wrappers.file import ContentFile
from network.canvas_session_manager import CanvasSession

from content_wrappers.url import ContentURL, ContentURLVideo, ContentURLAudio
from sorters.sorter_re import general_url_verification, web_video_resources, audio_file_resources, video_file_resources, \
    web_audio_resources


def web_video_identifier(link: str, local_session: CanvasSession, parent, root) -> Optional[ContentURLVideo]:

    if link is None:
        return None

    match_link = web_video_resources.match(link)

    if bool(match_link):

        return ContentURLVideo(match_link.group(), local_session, parent, root)

    return None


def web_audio_identifier(link: str, local_session: CanvasSession, parent, root) -> Optional[ContentURLAudio]:
    if link is None:
        return None

    match_link = web_audio_resources.match(link)
    if bool(match_link):

        return ContentURLAudio(match_link.group(), local_session, parent, root)

    return None

