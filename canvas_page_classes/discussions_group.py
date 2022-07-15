from core_canvas_classes.generic_page_component_node import PageComponentNode


class DiscussionsGroup(PageComponentNode):

    def __init__(self, session, component_html, tree_vis, parent, page_manifest: dict, content_manifest: dict,
                 junk_manifest: list,
                 count,
                 **kwargs):
        PageComponentNode.__init__(self, session, component_html, tree_vis, parent, page_manifest, content_manifest,
                                   junk_manifest,
                                   count,
                                   **kwargs)
