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


def rightSideView(t):
    queue = [t.root]
    result = []

    # while the queue is not empty
    while queue:
        length = len(queue)
        tempList = []
        count = 0

        # inner loop to populate tempList. this list helps us keep tack of the level being traversed
        while count < length:
            # pop first element from queue
            firstEl = queue.pop(0)
            # append popped value to tempList
            tempList.append(firstEl.value)

            # check if left child node exists
            if firstEl.left:
                queue.append(firstEl.left)

                # check if left child node exists
            if firstEl.right:
                queue.append(firstEl.right)

            count += 1

        # at this point, tempList contains nodes on the given level
        # then to answer the question, we simply take the last element in the list
        result.append(tempList[length - 1])

    return result


print(rightSideView(tree))
