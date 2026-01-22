class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, t=0):
        if self.parent:
            print('\t|__'.expandtabs(t) + self.data)
        else:
            print(self.data)
        if len(self.children)!=0:
            for child in self.children:
                child.print_tree(t + 4)

    def get_level(self):
        level = 0;                  # I learned how to use the debugging here WAHOOOOOO that felt nice
        p = self.parent
        while p:
            level+=1
            p = p.parent            # previous iterations was self.parent but self was not reassigned so the grand parent of the children end up
        return level                # becoming the parent of the children and was stuck in an endless loop.
                                    # reminds me of current = current.next in a linked list
    def to_dict(self):
        return {
            "id": str(id(self)),
            "value": self.data,
            "children": [child.to_dict() for child in self.children]
        }
    def to_graphviz(self):
        nodes = []
        edges = []

        def walk(node):
            nodes.append({
                "id": str(id(node)),
                "label": node.data
            })
            for child in node.children:
                edges.append({
                    "from": str(id(node)),
                    "to": str(id(child))
                })
                walk(child)

        walk(self)

        return {
            "kind": {"graph": True},
            "nodes": nodes,
            "edges": edges
        }


def build_product_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    return root

if __name__ == "__main__":
    tree = build_product_tree()
    tree.print_tree()


