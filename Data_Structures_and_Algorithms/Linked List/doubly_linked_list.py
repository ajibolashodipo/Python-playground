class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def push(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.tail = self.head
            self.length += 1
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.length += 1

    def print_list(self):
        arr = []
        curr = self.head
        while curr:
            arr.append(curr.data)
            curr = curr.next
        print(arr)
        return arr

    def insert(self, index, data):
        newNode = Node(data)
        if index == 1:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        else:
            curr = self.head
            # trace it. index-2 makes sense. you've got this
            for _ in range(index - 2):
                curr = curr.next
            future = curr.next
            curr.next = newNode
            newNode.prev = curr
            newNode.next = future
            # conditional is essential for inserting on the very last node. cos here, there is no future.prev
            # this conditional helps us look ahead
            if future:
                future.prev = newNode

    def delete(self, index):
        if index == 1:
            old_head = self.head
            self.head = old_head.next
            self.head.prev = None
            self.length -= 1
        else:
            curr = self.head
            # trace it. index-2 makes sense. you've got this
            for _ in range(index - 2):
                curr = curr.next
            # value of curr after the loop is on the node before the target
            target = curr.next
            future = target.next

            curr.next = future
            # this conditional helps us look ahead
            if future:
                future.prev = curr
            self.length -=1

    def reverse(self):
        pass

dll = DoublyLinkedList()
dll.push(2)
dll.push(3)
dll.push(4)
dll.push(5)
dll.insert(1, 8)
dll.insert(1, 5)
dll.insert(1, 8)
dll.insert(6, 228)
# dll.delete(1)
dll.delete(2)
dll.print_list()
