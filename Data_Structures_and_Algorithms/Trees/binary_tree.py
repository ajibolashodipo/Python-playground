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

    def preorder_print_iterative(self):
        curr = self.root
        stack = []
        # loop while current node is not null and length of stack is not empty
        while curr or len(stack):
            if curr:
                # for preorder, print before going on left side
                print(curr.value)
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                curr = curr.right

    def inorder_print_iterative(self):
        curr = self.root
        stack = []
        # loop while current node is not null and length of stack is not empty
        while curr or len(stack):
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                # for inorder, print before going on right side
                print(curr.value)
                curr = curr.right

    def breadth_first_traversal(self):
        # initialize the queue
        queue = []
        res = []
        node = self.root
        queue.append(node)
        # while root is not empty
        while queue:
            # pop the foremost node out and print it's value
            el = queue.pop(0)
            res.append(el.value)
            # check the left and right of said element and push those nodes (if they exist) into the queue
            if el.left:
                queue.append(el.left)
            if el.right:
                queue.append(el.right)
        print(res)
        return res


tree = BinaryTree(6)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(7)
tree.root.right.left = Node(8)
tree.root.right.right = Node(9)

tree.preorder_print()
tree.inorder_print()
tree.preorder_print_iterative()
tree.breadth_first_traversal()
