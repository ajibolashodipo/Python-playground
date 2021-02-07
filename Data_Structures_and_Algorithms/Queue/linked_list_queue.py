class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Queue:
    def __init__(self):
        self.top = None
        self.length = 0
        self.tail = None

    def enqueue(self, val):
        newNode = Node(val)

        # check if stack is full. essentially just check if newNode is null
        if not newNode:
            print("Stack overflow")
            return

        self.length += 1
        if self.top is None:
            self.top = newNode
            self.tail = self.top
        else:
            self.tail.next = newNode
            self.tail = newNode

    def dequeue(self):
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

q= Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(1)
q.enqueue(1)
q.enqueue(4)
q.dequeue()
q.dequeue()
q.printList()