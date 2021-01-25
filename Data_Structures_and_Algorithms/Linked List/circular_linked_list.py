class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.head.next = self.head
        else:
            # assign newNode's next to the current head
            newNode.next = self.head

            # initialize current head
            curr = self.head

            # loop until you get the last node
            while curr.next != self.head:
                curr = curr.next

            # value of curr at this point (after the loop) is the current final node
            # link next node of current to the prepended node
            curr.next = newNode

            # assign the new head to the new node
            self.head = newNode

    def append(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            # node must refer to itself for obvious reasons lool
            self.head.next = self.head

        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            # add new node
            curr.next = newNode
            newNode.next = self.head

    def delete(self, index):
        if index == 0:
            old_head = self.head
            new_head = self.head.next
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            # assign last's node's next to new head
            curr.next = new_head
            self.head = new_head

        # this block is redundant cos if index==1, the loop would simply not execute. which is exactly what we want
        # for this case.

        # elif index == 1:
        #     curr = self.head
        #     future = curr.next.next
        #     curr.next = future
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            # current value of curr at this point is the node before to the node to be deleted
            future = curr.next.next
            curr.next = future

    def print_list(self):
        first = self.head
        print(first.data)
        arr = [first.data]
        curr = first.next
        while curr != first:
            arr.append(curr.data)
            curr = curr.next
        print(arr)
        return


cll = CircularLinkedList()
cll.append(2)
cll.append(3)
cll.append(4)
cll.append(5)
cll.prepend(1)
cll.prepend(9)
cll.prepend(10)

cll.delete(0)
cll.delete(1)
cll.delete(2)
cll.print_list()
