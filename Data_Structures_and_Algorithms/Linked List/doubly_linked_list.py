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
            self.length -= 1

    def reverse(self):
        curr = self.head
        # what i am doing essentially is to traverse the node and swap the pointers.
        # you must understand though, that to move to the next node after this exercise requires you to use node.prev
        # as opposed to node.next cos pointers have been swapped prior, you get. :))

        while curr:
            # swap the pointers
            temp = curr.next
            curr.next = curr.prev
            curr.prev = temp

            # advance using curr.prev
            curr = curr.prev

            # assign the head pointer to last node
            # also note that we are using curr.next to look ahead as opposed to curr.prev cos these ahead nodes
            # have not been affected by pointer swaps. so things work as they should

            # we take extra steps in this conditional because the while loop condition only breaks when curr
            # becomes None. However in this case, we need the current value to be valid and the next value to
            # be None as this guarantees the rightful position of the head pointer
            if curr is not None and curr.next is None:
                self.head = curr


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
dll.reverse()
dll.print_list()
