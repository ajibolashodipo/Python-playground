# heap insertion
# heap deletion
# heap print
# heap heapify


class MaxHeap:

    def __init__(self):
        self.heap = [30, 20, 15, 5, 10, 12, 6]

    def insert(self, value):
        # append value to array
        self.heap.append(value)

        # find index of child index
        cIndex = len(self.heap) - 1

        # index of parent index
        pIndex = (cIndex - 1) // 2

        # if cIndex equals 0, it means we are at the root already, there is nothing to compare it to
        # also, the other condition sets the prerequisite for swapping
        while cIndex > 0 and self.heap[cIndex] > self.heap[pIndex]:
            print(cIndex, pIndex)

            # swap and assign old parent position to child
            cIndex = self._swap(cIndex, pIndex, self.heap)

            # recalculate parent index
            pIndex = (cIndex - 1) // 2

    def _swap(self, c, p, arr):
        arr[p], arr[c] = arr[c], arr[p]
        return p

    def printHeap(self):
        print(self.heap)

    def removeRoot(self):
        root = 0
        end = len(self.heap) - 1

        # swap array values of root and end
        self._yourSwap(root, end, self.heap)

        # pop element from array
        self.heap.pop()
        # initialize values for child nodes
        lChild = 2 * root + 1
        rChild = 2 * root + 2
        # now compare the temporary root with the larger of its 2 children and swap accordingly
        while lChild < end or rChild < end:

            # find maximum child node
            childMax = self._findMaxChild(lChild, rChild, self.heap)

            if childMax > root:
                # swap childMax and root. grab first element from returned tuple
                root = self._yourSwap(root, childMax, self.heap)[0]

                # go again. update values for new child nodes
                lChild = 2 * root + 1
                rChild = 2 * root + 2

    def _findMaxChild(self, l, r, arr):
        s = max(arr[l], arr[r])
        if s == arr[l]:
            return l
        return r

    def _yourSwap(self, a, b, arr):
        arr[b], arr[a] = arr[a], arr[b]
        return b, a


maxHeap = MaxHeap()

array = [40, 90, 45, 23, 78, 3]
array = [40]
for i in array:
    maxHeap.insert(i)

maxHeap.printHeap()
maxHeap.removeRoot()
maxHeap.printHeap()
