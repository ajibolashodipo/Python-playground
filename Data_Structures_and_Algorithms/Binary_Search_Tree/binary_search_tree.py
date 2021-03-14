# binary search tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # recursive insert
    def insert(self, data):
        # check if root is empty
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    # helper function
    def _insert(self, data, curr):
        if data < curr.data:
            # check if left node is empty
            if curr.left is None:
                curr.left = Node(data)
            # else recurse to the left node
            else:
                self._insert(data, curr.left)
        elif data > curr.data:
            # check if right node is empty
            if curr.right is None:
                curr.right = Node(data)
            else:
                self._insert(data, curr.right)

        # else condition checks for equality
        else:
            print("Value is already present in tree")

    def insert_2(self, target):
        def helper_insert(curr, target):
            if curr is None:
                newNode = Node(target)
                return newNode
                # return Node(target)
            else:
                if curr.data == target:
                    return curr
                elif curr.data < target:
                    curr.right = helper_insert(curr.right, target)
                else:
                    curr.left = helper_insert(curr.left, target)
            return curr

        root=helper_insert(self.root, target)

    # recursive search
    def find(self, data):
        res = self._find(data, self.root)
        # print(res)
        if res:
            print(f"{data} exists in Binary Search Tree")
        else:
            print(f"{data} does NOT exist in the BST")

    # helper function
    def _find(self, data, curr):
        if curr is None:
            return None
        else:
            if curr.data == data:
                return curr.data
            elif curr.data < data:
                return self._find(data, curr.right)
            else:
                return self._find(data, curr.left)

    def iterative_search(self, target):
        curr = self.root
        while curr:
            if curr.data == target:
                print(f"{target} exists in the BST")
                return
            elif curr.data > target:
                curr = curr.left
            else:
                curr = curr.right
        print(f"{target} does not exist in the BST")
        return

    def iterative_insert(self, data):
        # we need two pointers. one to keep track of the current Node. And the other to track the previous node
        curr = self.root
        prev = None
        # check that the root node isn't empty
        if curr is None:
            curr = Node(data)
            return
        # loop while curr is not None:
        while curr:
            if curr.data == data:
                print(f"{data} already exists in the tree")
                return
            elif curr.data < data:
                # move prev to curr
                prev = curr
                # then move curr to right
                curr = curr.right
            else:
                # move prev to curr
                prev = curr
                # then move curr to left
                curr = curr.left
        # when loop ends i.e curr becomes None, we then use prev pointer to decide on which side to add the new Node
        if prev.data > data:
            prev.left = Node(data)
        else:
            prev.right = Node(data)


bst = BinarySearchTree()
bst.insert_2(8)
bst.insert_2(1)
bst.insert_2(6)
bst.insert_2(13)
bst.insert_2(10)
bst.insert_2(16)
bst.iterative_insert(8)
bst.iterative_insert(1)
bst.iterative_insert(6)
bst.iterative_insert(13)
bst.iterative_insert(10)
bst.iterative_insert(16)
bst.find(6)
bst.find(8)
bst.find(81)
bst.iterative_search(6)
bst.iterative_search(8)
bst.iterative_search(81)
