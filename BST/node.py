
#Each node of the BST
class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BST(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, item):
        self.size = self.size + 1
        return self.addHelper(item, self.root)

    def addHelper(self, item, root):
        if root is None:
            root = Node(item)
            return root

        if item < root.value:
            root.left = self.addHelper(item, root.left)
        else:
            root.right = self.addHelper(item, root.right)

        return root

def pre_order_print(root):
    if not root:
        return
    print root.value
    pre_order_print(root.left)
    pre_order_print(root.right)


bst = BST()
bst.root = bst.add(5)
bst.root = bst.add(2)
bst.root = bst.add(7)
bst.root = bst.add(1)
bst.root = bst.add(4)
bst.root = bst.add(3)
bst.root = bst.add(6)
bst.root = bst.add(8)
pre_order_print(bst.root)
print "Size = " + str(bst.size)
