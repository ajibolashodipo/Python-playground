class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)


tree = BinaryTree(3)
tree.root.left = Node(6)
tree.root.right = Node(1)
tree.root.left.left = Node(9)
tree.root.left.right = Node(2)
tree.root.right.right = Node(4)


# tree.root.right.right = Node(9)


def level_order(t):
    queue = [(t.root, 1)]
    res = []

    while queue:
        el, l = queue.pop(0)

        res.append((el.value, l))

        if el.left:
            queue.append((el.left, l + 1))

        if el.right:
            queue.append((el.right, l + 1))

    dic = {}
    for v, i in res:
        if i not in dic:
            dic[i] = [v]
        else:
            dic[i].append(v)

    x = dic.values()
    return list(x)


print(level_order(tree))
