import re

from dotenv import load_dotenv
import os
from os.path import join, dirname
from config.read import read_re

dotenv_path = join(dirname(__file__), '../network/.env')
load_dotenv(dotenv_path)
instructure_root = os.environ.get("instructure_root")

expressions = read_re()


def mime_check(re_list):

    raw = [item.strip('.*\\.') for item in re_list]
    raw_string = "|".join(raw)
    return re.compile(raw_string, re.IGNORECASE)





def re_combiner(re_list):

    raw_string = "|".join(re_list)
    return re.compile(raw_string, re.IGNORECASE)

general_url_verification = re.compile(
    r'^(?:http|ftp)s?://' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
    r'localhost|' #localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)


ignore_links = re_combiner(expressions["ignore_links_regex"])

resource_node_regex = re.compile(expressions["resource_node_re"])

document_content_regex = re_combiner(expressions["document_content_regex"])

image_content_regex = re_combiner(expressions["image_content_regex"])

canvas_user_file_content_regex = re.compile(instructure_root + expressions["canvas_user_file_content_regex"])

canvas_file_content_regex = re.compile(instructure_root + expressions["canvas_file_content_regex"])

web_video_resources = re_combiner(expressions["web_video_resources_regex"])

video_file_resources = re_combiner(expressions["video_file_resources_regex"])

web_audio_resources = re_combiner(expressions["web_audio_resources_regex"])

audio_file_resources = re_combiner(expressions["audio_file_resources_regex"])

additional_ignore_list = re_combiner(expressions["additional_ignore_list_regex"])

mime_check_image = mime_check(expressions["image_content_regex"])

mime_check_document = mime_check(expressions["document_content_regex"])

