from abc import ABC, abstractmethod

from PositionalList.PositionalList import PositionalList


class PriorityQueueBase(ABC):
    class Item:
        def __init__(self, item, priority):
            self.item = item
            self.priority = priority

        def __lt__(self, other):
            return self.priority < other.priority

        def __le__(self, other):
            return self.priority <= other.priority

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def min(self):
        pass

    @abstractmethod
    def removeMin(self):
        pass


class PriorityQueue(PriorityQueueBase):
    def __init__(self, sorted=False):
        self.data = PositionalList()
        self.sorted = sorted

    def __len__(self):
        return len(self.data)

    def add(self, item, priority):
        toAdd = self.Item(item, priority)
        if self.sorted:
            if len(self.data) == 0:
                self.data.addFirst(toAdd)
            elif self.data.first().node.item.priority > priority:
                self.data.addBefore(self.data.first(), toAdd)
            else:
                next = self.data.first()
                while (
                    self.data.after(next) is not None
                    and self.data.after(next).node.item.priority < priority
                ):
                    next = self.data.after(next)
                self.data.addAfter(next, toAdd)
        else:
            self.data.addLast(toAdd)

    def _min(self, removeMin=False):
        if self.data.length == 0:
            raise ValueError("no items in queue")
        if self.sorted:
            minPosition = self.data.first()
        else:
            minPosition = self.data.first()
            for position in self.data:
                if position.node.item.priority < minPosition.node.item.priority:
                    minPosition = position
        if removeMin:
            self.data.delete(minPosition)
        return minPosition.node.item.item, minPosition.node.item.priority

    def min(self):
        return self._min()

    def removeMin(self):
        return self._min(removeMin=True)
