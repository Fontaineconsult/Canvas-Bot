from typing import Optional

from content_wrappers.externalcontent import WebDocumentApplication
from network.canvas_session_manager import CanvasSession
import re
from config.read import read_re
from additional_page_classes.boxpage import BoxPage
from sorters.sorter_re import google_doc_regex

additional_page_re = read_re()['additional_page_regex']

additional_page_dict = {

    re.compile(additional_page_re['BoxPage']): BoxPage

}


def additional_page_identifier(local_session: CanvasSession,
                               link: str,
                               root,
                               parent,
                               page_manifest,
                               content_manifest,
                               junk_manifest,
                               **kwargs
                        ):

    for each in additional_page_dict:
        if each.match(link):
            node = additional_page_dict[each](
                local_session,
                link,
                root,
                parent,
                page_manifest,
                content_manifest,
                junk_manifest,
                **kwargs
            )

            return node


def web_document_application_identifier(link: str, local_session: CanvasSession, parent, root) -> Optional[WebDocumentApplication]:
    # not using yet
    if link is None:
        return None

    match_link = google_doc_regex.match(link)
    if bool(match_link):
        return WebDocumentApplication(match_link.group(), local_session, parent, root)
    return None