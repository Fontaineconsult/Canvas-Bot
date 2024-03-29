


class Manifest:

    def __init__(self):
        self.manifest = dict()

    def __len__(self):
        return len(self.manifest.keys())

    def add_item_to_manifest(self, node):

        if self.manifest.get(node.url) is None:
            self.manifest[node.url] = list()
            self.manifest[node.url].append(node)
        else:
            self.manifest[node.url].append(node)

    def get_item_from_manifest(self, url, root):

        if self.manifest.get(url) is not None:
            for node in self.manifest[url]:
                if node.root == root:
                    return node
            return None
        return None

    def keys(self):
        return self.manifest.keys()

    def exists(self, link, node) -> bool:
        if link not in self.manifest.keys():
            return False
        for ex_node in self.manifest[link]:
            if ex_node.root == node.root:
                return True
        return False

    def get_manifest(self):
        return self.manifest

    def print_manifest(self):
        for item in self.manifest:
            print(item, self.manifest[item])

    def get_content(self):
        return_list = list()
        for item in self.manifest.keys():
            return_list.append(self.manifest[item][0])
        return return_list

    def update_item_in_manifest(self, link, node):
        pass



