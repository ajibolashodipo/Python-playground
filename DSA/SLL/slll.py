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

    def printList(self):
        current = self.head
        container = []
        while current:
            container.append(current.data)
            current = current.next
        return container

    def printList_Recursive(self):
        current = self.head
        container = []

        def helperFunction(curr):
            if curr is not None:
                container.append(curr.data)
                helperFunction(curr.next)

        helperFunction(current)
        return container

    def my_count(self):
        current = self.head

        def counter_helper(current):
            if current is None:
                return 0
            else:
                return counter_helper(current.next) + 1

        count = counter_helper(current)
        print(count)
        return count

    def add_elements(self):
        current = self.head

        def add_helper(current):
            if current is None:
                return 0
            else:
                return add_helper(current.next) + int(current.data)

        res = add_helper(current)
        print(res)
        return res


aj1 = SinglyLinkedList()
aj1.push("111")
aj1.push("111")
aj1.push("111")
aj1.push("222")
print(aj1.printList())
print(aj1.printList_Recursive())
aj1.my_count()
aj1.add_elements()
