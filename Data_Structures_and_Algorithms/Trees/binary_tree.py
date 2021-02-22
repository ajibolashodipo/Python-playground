class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def preorder_print(self):
        curr = self.root
        print(curr.left.value)
        arr = []

        def preorder_helper(curr):
            if curr:
                arr.append(curr.value)
                preorder_helper(curr.left)
                preorder_helper(curr.right)

        preorder_helper(curr)
        print(arr)
        return arr

    def inorder_print(self):
        curr = self.root
        arr = []

        def inorder_helper(curr):
            if curr:
                inorder_helper(curr.left)
                arr.append(curr.value)
                inorder_helper(curr.right)

        inorder_helper(curr)
        print(arr)
        return




tree = BinaryTree(6)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(7)
tree.root.right.left = Node(8)
tree.root.right.right = Node(9)

tree.preorder_print()
tree.inorder_print()
