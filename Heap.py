from PriorityQueue import PriorityQueueBase


class Heap(PriorityQueueBase):
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def _leftIndex(self, index):
        return 2 * index + 1

    def _rightIndex(self, index):
        return 2 * index + 2

    def _parentIndex(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.data[index1], self.data[index2] = self.data[index2], self.data[index1]

    def _upHeap(self, index=None):
        if index is None:
            index = len(self)
        if self.data[self._parentIndex(index)] < self.data[index]:
            self._swap(self._parentIndex(index), index)
            self._upHeap(index=self._parentIndex(index))

    def _downHeap(self, index=None):
        if index is None:
            index = 0
        if (
            self.data[self._leftIndex(index)] < self.data[index]
            and self.data[self._leftIndex(index)] < self.data[self._rightIndex(index)]
        ):
            self._swap(self._leftIndex(index), index)
            self._downHeap(index=self._leftIndex(index))
        elif (
            self.data[self._rightIndex(index)] < self.data[index]
            and self.data[self._leftIndex(index)] > self.data[self._rightIndex(index)]
        ):
            self._swap(self._rightIndex(index), index)
            self._downHeap(index=self._rightIndex(index))

    # PUBLIC METHODS

    def add(self, item, priority):
        self.data.append(self.Item(item, priority))
        self._upHeap()

    def min(self):
        if len(self) == 0:
            raise ValueError("empty queue")
        return self.data[0][0], self.data[0][1]

    def removeMin(self):
        min = self.min()
        self.data[0] = self.data[-1]
        self._downHeap()
        return min
