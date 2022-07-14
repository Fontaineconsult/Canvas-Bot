from network.canvas_session_manager import CanvasSession
import re
from config.read import read_re
from additional_page_classes.boxpage import BoxPage

from core_canvas_classes.manifest import Manifest

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











