class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.tail = None
        self.length = 0

    def push(self, val):
        newNode = Node(val)
        self.length += 1
        if self.top is None:
            self.top = newNode
            self.tail = self.top
        else:
            newNode.next = self.top
            self.top = newNode

    def pop(self):
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


s= Stack()
s.push(3)
s.push(23)
s.push(13)
s.push(43)
s.push(53)
s.pop()
print(s.isEmpty())
s.printList()
