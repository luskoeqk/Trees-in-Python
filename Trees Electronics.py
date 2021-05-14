# codebasics

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent

        return level


    def tree_print(self):
        spaces = ' ' * self.get_level() * 4
        prefix = spaces + "\__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.tree_print()


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Asus"))
    laptop.add_child(TreeNode("Thinkpad"))


    cellphone = TreeNode("Cell Phone")
    cellphone.add_child((TreeNode("iPhone")))
    cellphone.add_child((TreeNode("Android")))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Samsung"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    return root


root = build_product_tree()
root.tree_print()
print(root.get_level())












