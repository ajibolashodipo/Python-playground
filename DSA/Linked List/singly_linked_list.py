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

    def max_val(self):
        temp_max = int(self.head.data)
        current = self.head
        while current.next:
            temp_max = max(temp_max, int(current.next.data))
            current = current.next
        print(temp_max)
        return temp_max

    def search_recursive(self, key):
        current = self.head

        def search_helper(current, key):
            if current is None:
                return False
            if key == current.data:
                return True
            return search_helper(current.next, key)

        res = search_helper(current, key)
        print(res)
        return res

    def unshift(self, data):
        #          create a new node
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def insert(self, index, data):
        newNode = Node(data)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        print(f"ajibola {current.data}")
        future = current.next
        current.next = newNode
        newNode.next = future

    def sorted_insert(self, value):
        newNode = Node(value)
        current = self.head

        # to insert at zeroth index
        if newNode.data <= current.data:
            newNode.next = self.head
            self.head = newNode
            return
        # to insert at final index
        if newNode.data >= self.tail.data:
            self.tail.next = newNode
            self.tail = newNode
            return
        # to insert within the linked list
        while current.next:
            prev = current
            current = current.next
            if newNode.data < current.data:
                prev.next = newNode
                newNode.next = current
                return

    def is_sorted(self):
        current = self.head

        while current.next:
            prev = current
            current = current.next
            if prev.data > current.data:
                print("list is not sorted")
                return False
        print("list is sorted")
        return True

    def remove_duplicates(self):

        current = self.head
        forward = current.next
        while forward:
            if current.data != forward.data:
                current = forward
                forward = forward.next

            else:
                current.next = forward.next
                forward = forward.next

    def reverse(self):
        # using 3 sliding pointers that move together. quite easy to understand. you've got this
        f_next = self.head
        curr = None
        prev = None
        while f_next:
            prev = curr
            curr = f_next
            f_next = f_next.next
            curr.next = prev
        self.head = curr

    def reverse_recursion(self):
        # quite tough at first; requires some patience
        # actual link reversal is performed while recursive calls are returning
        def reverse_helper(q, p):
            if p is not None:
                reverse_helper(p, p.next)
                p.next = q
            else:
                self.head = q

        return reverse_helper(None, self.head)

    def concatenate(self, second):
        # using the tail pointer
        self.tail.next = second.head
        self.tail = second.tail
        # or you could just start from the head. takes longer computational time though. and is probably needless as
        # this is the whole point of the tail pointer in the first place

    def is_loop_floyd(self):
        # here we use two pointers. one fast one and one slow one. if they meet at any point, means a loop exists
        p = self.head
        q = self.head

        # if any of the below are None, it means there is no loop in the linked list as a tail points to None.
        while p and q and q.next:
            p = p.next
            q = q.next.next

            if p == q:
                return True

        return False

    def is_loop_2(self):
        s = set()
        temp = self.head
        while temp:
            if temp in s:
                return True
            s.add(temp)
            print(temp)
            temp = temp.next
        return False

    def display_circular(self):
        first = self.head
        print(first.data)
        arr = [first.data]
        curr = first.next
        while curr != first:
            arr.append(curr.data)
            curr = curr.next
        print(arr)
        return


aj1 = SinglyLinkedList()
aj1.push(1)
aj1.push(5)
aj1.push(111)
aj1.push(222)
aj1.unshift(455)
aj1.insert(1, 3)
aj1.sorted_insert(187)

aj1.remove_duplicates()
print(aj1.printList())
# aj1.reverse_recursion()
print(aj1.printList_Recursive())
aj1.my_count()
aj1.add_elements()
aj1.max_val()
aj1.is_sorted()

# second linked list for concatenation
# second_ll = SinglyLinkedList()
# second_ll.push(1)
# second_ll.push(2)
# second_ll.push(3)

print(aj1.printList_Recursive())
# aj1.concatenate(second_ll)
print(aj1.printList_Recursive())
print(aj1.is_loop_2())


tobi = SinglyLinkedList()
tobi.push(10)
tobi.push(1)
tobi.push(2)
tobi.push(3)
tobi.push(4)
# tobi.printList()
tobi.display_circular()
