from core_canvas_classes.generic_page_node import PageNode
from network.canvas_session_manager import CanvasSession
from additional_page_classes.external_page import ExternalPage
from sorters.sorting_tools import ignore_url, is_url_valid


def external_resource_identifier(local_session: CanvasSession,
                                 link: str,
                                 root,
                                 parent,
                                 page_manifest: dict,
                                 content_manifest: dict,
                                 junk_manifest: list,
                                 **kwargs) -> [PageNode, str]:


    if link is None:
        return None

    if is_url_valid(link) is False:
        return None

    if ignore_url(link) is True:
        return None

    return ExternalPage(local_session,
                        link,
                        root,
                        parent,
                        page_manifest,
                        content_manifest,
                        junk_manifest,
                        **kwargs)











