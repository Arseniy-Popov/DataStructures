from collections.abc import Container, Sized


class Heap(Container, Sized):
    """
    Priority queue implemented with the heap data structure.
    Allows for retrieval of the smallest element and insertions
    in O(logn) time, as well as constant time smallest element
    access. Ordering of the elements can be customized with the
    optional 'key' callable. Comparisons utilize the __lt__ method.
    
    Provides the .push, .peek, .pop, __len__, __contains__,
    and __repr__ methods.
    """

    class _Item:
        """
        Used to populate the underlying storage array with pairs
        of items and keys so that keys are cached.
        """

        def __init__(self, item, key=None):
            self._item = item
            self._key = key

        def __lt__(self, other):
            if not self._key:
                return self._item < other._item
            return self._key < other._key

    def __init__(self, key=None):
        self._array = []
        self._key = key or (lambda x: x)

    def __len__(self):
        return len(self._array)

    def __contains__(self, item):
        return any(x._item == item for x in self._array)

    def __repr__(self):
        return f"<Heap of lenght {len(self)}, min: {self.peek()}>"

    def push(self, item):
        self._array.append(self._Item(item, key=self._key(item)))
        self._restore_order_insertion()

    def peek(self):
        if not len(self):
            raise IndexError
        return self._array[0]._item

    def pop(self):
        result, self._array[0] = self.peek(), self._array[-1]
        self._array.pop()
        self._restore_order_deletion()
        return result

    # Non-public utilities

    def _index_valid(self, index):
        if index > len(self) - 1 or index < 0:
            return None
        return index

    def _left_child(self, index):
        return self._index_valid(index * 2 + 1)

    def _right_child(self, index):
        return self._index_valid(index * 2 + 2)

    def _parent(self, index):
        return self._index_valid((index - 1) // 2)

    def _item(self, index):
        return self._array[index]

    def _swap(self, index1, index2):
        self._array[index1], self._array[index2] = (
            self._array[index2],
            self._array[index1],
        )

    def _min_child(self, index):
        if self._left_child(index) is None and self._right_child(index) is None:
            return None
        elif self._right_child(index) is None:
            return self._left_child(index)
        else:
            return min(
                self._left_child(index), self._right_child(index), key=self._item
            )

    def _restore_order_insertion(self):
        index = len(self._array) - 1
        while self._parent(index) is not None and not self._item(
            self._parent(index)
        ) < self._item(index):
            self._swap(index, self._parent(index))
            index = self._parent(index)

    def _restore_order_deletion(self):
        index = 0
        while not (
            self._min_child(index) is None
            or not self._item(self._min_child(index)) < self._item(index)
        ):
            min_child = self._min_child(index)
            self._swap(min_child, index)
            index = min_child
