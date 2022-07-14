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
from sorters.sorter_re import resource_node_regex

from sorters.sorting_tools import is_url_valid

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

def canvas_resource_identifier(local_session: CanvasSession,
                               link: str,
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

    if link is None:
        return None

    if isinstance(link, str):

            if link in junk_manifest:
                return None

            if re.search(re.compile("courses/[0-9]{0,7}/modules/items"), link):

                if not is_url_valid(link):
                    link = os.environ.get("instructure_root") + link

                    if link in junk_manifest:
                        return None

                get_url = local_session.requests_get(link)
                if get_url:
                    if len(get_url.history) == 0:

                        return Item(local_session,
                                    link,
                                    root,
                                    parent,
                                    page_manifest,
                                    content_manifest,
                                    junk_manifest,
                                    **kwargs)

                    else:
                        for request in get_url.history:

                            if request.status_code == 302:

                                match_link = resource_node_regex.match(request.headers['location'])

                                if bool(match_link):
                                    if match_link.group() in page_manifest.keys():
                                        return None

                                    if link not in junk_manifest:
                                        junk_manifest.append(link)

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
                                    junk_manifest.append(link)
                                    junk_manifest.append(cleaned_link)
                                    return str(cleaned_link)


            match_link = resource_node_regex.match(link)

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

