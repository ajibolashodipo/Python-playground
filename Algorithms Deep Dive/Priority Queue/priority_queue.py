class PriorityQueue:
    def __init__(self):
        self._heap = [100, 90, 80, 50, 40, 7]

    def size(self):
        return len(self._heap)

    def isEmpty(self):
        return self._heap == []

    def peek(self):
        return self._heap[0]

    def push(self, value):

        # append value to heap to maintain completeness
        self._heap.append(value)

        # rename heap for easier access
        heap = self._heap

        # track index of newly assigned element
        idx = len(self._heap) - 1

        # compare with parent nodes

        # greater than 0 as opposed to >=0 cos when idx becomes 0 in the loop, it means idx is already at the root
        # so that's our cue to exit the loop since idx is clearly the maximum value (in max heap)
        while idx > 0:
            parent = (idx - 1) // 2
            if heap[idx] > heap[parent]:
                # swap elements
                self._swap(heap, idx, parent)

                # update idx
                idx = parent
            else:
                break
        return self.size()

    def _swap(self, heap, idx, par):
        heap[idx], heap[par] = heap[par], heap[idx]
        return

    def pop(self):

        idx = 0
        last = len(self._heap) - 1

        # for easier access
        heap = self._heap

        # swap first element and last
        self._swap(heap, idx, last)

        # initialize loop
        while True:

            # initialize left and right child nodes of current index
            left = (idx * 2) + 1
            right = (idx * 2) + 2

            # return local maximum of child nodes
            localMax = self._getMaxAtLevel(left, right)

            # if localMax is none, it means the node has no children; a waste of our time. Hence, we break
            if localMax is None:
                break

            # proceed with core logic
            if heap[idx] < heap[localMax]:

                # swap current idx with localMax
                self._swap(heap, idx, localMax)

                # update idx to localMax
                idx = localMax
            else:
                break

            # pop removed element from heap
            return heap.pop()

    def _getMaxAtLevel(self, l, r):

        # check in case left or right children go out of bounds
        if l < len(self._heap) and r < len(self._heap):
            if self._heap[l] > self._heap[r]:
                return l
            return r

        elif l < len(self._heap):
            return l

        # we need not check for just r cos the completeness condition of heaps
        # guarantees that if right child exists, left child must exist too
        else:
            return None


h = PriorityQueue()
print(h.peek())
h.push(1000)
h.push(89)
print(h.peek())
print(h._heap)
print(h.pop())
print(h.pop())
print(h._heap)
