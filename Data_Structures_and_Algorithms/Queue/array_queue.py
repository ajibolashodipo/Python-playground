# With Arrays, we can implement queues in 2 ways

# 1. Queue using one pointer
# This is akin to using a regular array. FIFO. Insertions are in constant time . However, deletions are
# in O(n) time. Not very desirable

# 2. Queue using 2 pointers
# Similar to the above method. Just this it optimizes for deletion. Instead of moving all elements leftward
# upon deletion, We replace the deleted element with None and maintain a variable that points to the new first element

# First seems trivial so i shall implement the second


class Queue:
    def __init__(self):
        self.items = []

        # self.length = 0. we can use length to track the real time length of queued - dequeue to get the length.
        # or just use another pointer self.rear. its position changes during an enqueue but not during a dequeue
        self.rear = 0
        self.front = 0

    def enqueue(self, data):
        self.items.append(data)
        self.length += 1
        self.rear += 1

    def dequeue(self):
        dqd = self.items[self.front]
        # point current list[self.front] to None
        self.items[self.front] = None
        # then move it by one
        self.front += 1
        self.length -= 1
        print(dqd)
        return dqd

    def isFull(self):
        # wont be full exactly cos it's a dynamic array'
        pass

    def isEmpty(self):
        # return self.length == 0
        # or
        return self.front == self.rear

    def printItems(self):
        print(self.items)


q = Queue()
q.enqueue(1)
q.enqueue(3)
q.enqueue(5)
q.enqueue(7)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
print(q.isEmpty())
q.printItems()
