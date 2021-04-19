# imported previously implemented llist code
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        newNode = Node(val)
        self.length += 1
        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode

            # for circular linked list. could be wrong btw
            # self.tail.next = self.head
            # self.head = newNode

    def printList(self):
        current = self.head
        container = []
        while current:
            container.append(current.data)
            current = current.next
        return container

    # linked list m,n reversals. reverse a segment of a linked list
    # 1,2,3,4,5
    # m=2, n=4
    # 1,4,3,2,5
    def custom_reversal(self, m, n):
        # keep track of (m-1)th position

        # for robustness, we cannot assign this variable prevInit here. just in case the question requires
        # that we reverse the whole linked list. in this case, m is 1 and so
        # the for loop on line 49 does not run

        # prevInit = None
        start = self.head

        # linked list begins from index 1 hence the for loop starting from 1 below.
        # get index m as well as m-1
        for _ in range(1, m):
            prevInit = start
            start = start.next

        # initialize pointers for reversal
        forward = start
        curr = None
        # prev = None

        for _ in range(m, n + 1):
            if forward.next:
                prev = curr
                curr = forward
                forward = forward.next
                curr.next = prev
                print(forward.data)

        # understand that the forward pointer stores the address of n+1th node

        # edge case for m=1 (where m is equal to the head node. recall that in this case,
        # prevInit will not exist as the first for loop will not evaluate)
        if m > 1:

            # assign m-1th next node (prevInit) to curr
            prevInit.next = curr

            # assign mth next node to forward
            start.next = forward

            return self.head

        # implement edge case later. (THIS IS INCOMPLETE)
        else:

            self.head = curr
            return self.head


lst = SinglyLinkedList()
lst.push(1)
lst.push(2)
lst.push(3)
lst.push(4)
lst.push(5)

print(lst.printList())
lst.custom_reversal(1, 5)
print(lst.printList())
