from treelib import Node, Tree


class CanvasTree:

    def __init__(self):
        self.tree = Tree()


    def init_node(self, root):
        self.tree.create_node(str(root), str(id(root)))

    def add_node(self, node):
        node_name = str(node)
        node_value = str(id(node))
        parent = str(id(node.parent))
        self.tree.create_node(node_name, node_value, parent)

    def show_nodes(self):
        return self.tree.show()