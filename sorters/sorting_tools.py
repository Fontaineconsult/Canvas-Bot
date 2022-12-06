import mimetypes
from mimetypes import MimeTypes
import re
from urllib.parse import urljoin, urlparse
from config.read import read_config
requests_settings = read_config()

from sorters.sorter_re import ignore_links, resource_node_regex, document_content_regex, \
    image_content_regex, canvas_file_content_regex, web_video_resources, video_file_resources, \
    web_audio_resources, audio_file_resources, additional_ignore_list, general_url_verification, \
    canvas_user_file_content_regex

mimes = mimetypes.MimeTypes()

for new_type in read_config()['added_mimetypes']:
    mime_type, ext = new_type.split("|")
    mimetypes.add_type(mime_type, ext)


def is_url_valid(url):

    return re.match(general_url_verification, url) is not None



def ignore_url(url):

    if url is None:
        return False

    combined_re = re.compile('|'.join([f"({audio_file_resources.pattern})",
                                       f"({ignore_links.pattern})",
                                       f"({document_content_regex.pattern})",
                                       f"({canvas_file_content_regex.pattern})",
                                       f"({canvas_user_file_content_regex.pattern})",
                                       f"({web_video_resources.pattern})",
                                       f"({audio_file_resources.pattern})",
                                       f"({video_file_resources.pattern})",
                                       f"({image_content_regex.pattern})",
                                       f"({web_audio_resources.pattern})",
                                       f"({additional_ignore_list.pattern})"
                                       ]))

    return combined_re.match(url) is not None

def get_mime_type(link, note=None):

    clean_url = urljoin(link, urlparse(link).path)
    extension = f".{clean_url.split('.')[-1]}"
    # look for types that mimetypes doesn't have first
    for added_type in read_config()['added_mimetypes']:
        mime_type_new, ext = added_type.split("|")
        if extension == ext:
            return mime_type_new

    return mimes.guess_type(clean_url, strict=False)[0]

