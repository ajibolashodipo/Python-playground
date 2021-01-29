class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):
        newNode = Node(val)

        if self.head is None:
            self.head = newNode
            self.tail = self.head

        else:
            self.tail.next = newNode
            self.tail = newNode

    def print_list(self):
        arr = []
        curr = self.head
        while curr:
            arr.append(curr.data)
            curr = curr.next

        print(arr)
        return arr

    def find_middle_of_list(self):
        p = self.head
        q = self.head

        while q:
            # look ahead
            q = q.next
            # check if it's safe to proceed
            if q:
                # look ahead again
                q = q.next
            # check again
            if q:
                p = p.next

        # then print the value of p
        print(f'the middle value is {p.data}')
sll = SinglyLinkedList()
sll.push(1)
sll.push(2)
sll.push(3)
sll.push(4)
sll.push(5)
sll.push(6)
sll.push(7)
sll.print_list()
sll.find_middle_of_list()
