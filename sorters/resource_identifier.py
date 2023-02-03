import re
from urllib.parse import urljoin, urlparse

from dotenv import load_dotenv
import os
from os.path import join, dirname
from network.canvas_session_manager import CanvasSession
from canvas_page_classes.assignment import Assignment
from canvas_page_classes.page import Page
from canvas_page_classes.quiz import Quiz
from canvas_page_classes.discussion import Discussion
from canvas_page_classes.item import Item
from core_canvas_classes.generic_page_node import PageNode

from sorters.file_content_identifier import canvas_file_content_regex
from sorters.sorter_re import resource_node_regex, bad_redirects

from sorters.sorting_tools import is_url_valid
from tools.canvas_api import get_module_item

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

def canvas_resource_identifier(local_session: CanvasSession,
                               input_link: str,
                               root,
                               parent,
                               page_manifest: dict,
                               content_manifest: dict,
                               junk_manifest: list,
                               **kwargs) -> [PageNode, str]:

    resource_scaffold_key = {
        "pages/": Page,
        "quizzes/": Quiz,
        "discussion_topics/": Discussion,
        "assignments/": Assignment,

    }

    if input_link is None:
        return None

    if isinstance(input_link, str):

            if input_link in junk_manifest:
                return None

            if re.search(re.compile("courses/[0-9]{0,7}/modules/items"), input_link):

                if not is_url_valid(input_link):
                    input_link = os.environ.get("instructure_root") + input_link

                    if input_link in junk_manifest:
                        return None

                get_url = local_session.requests_get(input_link)


                if get_url:

                    if len(get_url.history) == 0:

                        return Item(local_session,
                                    input_link,
                                    root,
                                    parent,
                                    page_manifest,
                                    content_manifest,
                                    junk_manifest,
                                    **kwargs)

                    else:

                        for request in get_url.history:

                            if request.status_code == 302:
                                if bad_redirects.match(request.headers['location']):
                                    redirected_url = get_module_item(root.parent.canvas_course_id, parent.module_id, input_link.split("/")[-1])
                                    match_link = resource_node_regex.match(redirected_url)
                                    match_link_file = canvas_file_content_regex.match(redirected_url)

                                    if not bool(match_link) or not bool(match_link_file):
                                        return redirected_url

                                else:
                                    match_link = resource_node_regex.match(request.headers['location'])


                                if bool(match_link):

                                    if match_link.group() in page_manifest.keys():
                                        return None

                                    if input_link not in junk_manifest:
                                        junk_manifest.append(input_link)

                                    node = resource_scaffold_key[match_link.groups()[0]]

                                    new_node = node(local_session,
                                                    match_link.group(),
                                                    root,
                                                    parent,
                                                    page_manifest,
                                                    content_manifest,
                                                    junk_manifest,
                                                    **kwargs)
                                    return new_node

                                match_link_file = canvas_file_content_regex.match(request.headers['location'])

                                if bool(match_link_file):
                                    cleaned_link = urljoin(request.headers['location'],
                                                           urlparse(request.headers['location']).path)
                                    junk_manifest.append(input_link)
                                    junk_manifest.append(cleaned_link)
                                    return str(cleaned_link)






            match_link = resource_node_regex.match(input_link)
            if bool(match_link):

                node = resource_scaffold_key[match_link.groups()[0]]

                return node(local_session,
                            match_link.group(),
                            root,
                            parent,
                            page_manifest,
                            content_manifest,
                            junk_manifest,
                            **kwargs)

