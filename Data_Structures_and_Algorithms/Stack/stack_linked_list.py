class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, val):
        newNode = Node(val)

        # check if stack is full. essentially just check if newNode is null
        if not newNode:
            print("Stack overflow")
            return

        self.length += 1
        if self.top is None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode

    def pop(self):
        # check for empty stack
        if self.isEmpty():
            print("Stack is empty")
            return -1
        # do the damn work
        old_head = self.top
        self.top = self.top.next
        return old_head.data

    def isEmpty(self):
        if self.top: return False
        return True

    def printList(self):
        current = self.top
        container = []
        while current:
            container.append(current.data)
            current = current.next
        print(container)
        return container


s = Stack()
# s.push(3)
# s.push(23)
# s.push(13)
# s.push(43)
# s.push(53)
s.pop()
print(s.isEmpty())
s.printList()
