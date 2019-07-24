from PriorityQueue.PriorityQueue import PriorityQueueBase


class Heap(PriorityQueueBase):
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def _checkIndex(self, index):
        if index > len(self) - 1:
            return None
        else:
            return index 
        
    def _left(self, index):
        result = 2 * index + 1
        return self._checkIndex(result)
        
    def _right(self, index):
        result = 2 * index + 2
        return self._checkIndex(result)

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.data[index1], self.data[index2] = self.data[index2], self.data[index1]

    def _upHeap(self, index=None):
        """ Recursively swap items from leaf to root. """
        if index is None:
            index = len(self) - 1 
        if self.data[self._parent(index)] > self.data[index] and index != 0:
            self._swap(self._parent(index), index)
            self._upHeap(index=self._parent(index))

    def _downHeap(self, index=None):
        """ Recursively swap items from root to leaf. """
        if index is None:
            index = 0
        if 
        
    # PUBLIC METHODS

    def add(self, item, priority):
        self.data.append(self.Item(item, priority))
        self._upHeap()

    def min(self):
        if len(self) == 0:
            raise ValueError("empty queue")
        return self.data[0].item, self.data[0].priority

    def removeMin(self):
        min = self.min()
        self.data[0] = self.data.pop()
        self._downHeap()
        return min
