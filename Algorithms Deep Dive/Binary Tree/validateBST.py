class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)


tree = BinaryTree(12)
tree.root.left = Node(7)
tree.root.right = Node(18)
tree.root.left.left = Node(5)
tree.root.left.right = Node(9)
tree.root.right.right = Node(29)


def recurse(node, arr):
    if node is None:
        return
    recurse(node.left, arr)
    arr.append(node.value)
    recurse(node.right, arr)


def validateBST(tree):
    root = tree.root
    arr = []
    recurse(root, arr)
    print(arr)
    # iterate through list
    for j in range(len(arr) - 1):

        # duplicate values do not exist in this particular question
        if arr[j + 1] <= arr[j]:
            return False

    return True


print(validateBST(tree))
