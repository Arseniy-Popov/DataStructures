import collections.abc


class Deque(collections.abc.Sequence):
    """
    Double-ended queue supporting constant time insertions and deletions
    on either end as well as constant time indexing.
    
    Provides the .append, .appendLeft, .pop, .popLeft, __len__, and __getitem__
    methods by itself, and inherits __contains__, __iter__, __reversed__,
    .index, and .count from the collections.abc.Sequence abstract base class.
    """

    _initialSize = 10
    _resizeFactor = 2
    _shrinkThreshold = 0.5

    # Private utilities

    def _getArrayIndex(self, index):
        """
        Get index of the underlying circular array
        corresponding to the perceived deque index.  
        """
        return (self._headIndex + index) % len(self._array)

    def _resize(self):
        shrinkIfSmaller = self._shrinkThreshold * len(self._array) / self._resizeFactor
        postShrinkSize = len(self._array) / self._resizeFactor
        if len(self) == len(self._array):  # expand array
            newArray = len(self._array) * self._resizeFactor * [None]
        elif (
            len(self) <= shrinkIfSmaller and postShrinkSize >= self._initialSize
        ):  # shrink array
            newArray = int(len(self._array) / self._resizeFactor) * [None]
        else:  # no resize
            return
        for index, value in enumerate(self):
            newArray[index] = value
        self._array = newArray
        self._headIndex = 0

    # Accessor methods

    def __len__(self):
        return self._len

    def __getitem__(self, index):
        index = index if index >= 0 else len(self) + index
        if not 0 <= index < len(self):
            raise IndexError
        return self._array[self._getArrayIndex(index)]

    def __repr__(self):
        return f"<Deque {[i for i in self]}>"

    # Modifier methods

    def __init__(self, iterable=None):
        self._array = self._initialSize * [None]
        self._headIndex = 0
        self._len = 0
        if iterable:
            for item in iterable:
                self.append(item)

    def __setitem__(self, index, value):
        self._array[self._getArrayIndex(index)] = value

    def _append(self, value, left=False):
        self._resize()
        if left:
            index = -1
        else:
            index = len(self)
        self._array[self._getArrayIndex(index)] = value
        self._len += 1
        if left:
            self._headIndex = (self._headIndex - 1) % len(self._array)

    def append(self, value):
        self._append(value)

    def appendLeft(self, value):
        self._append(value, left=True)

    def _pop(self, left=False):
        if not len(self):
            raise IndexError("pop from empty array")
        self._resize()
        if left:
            index = 0
        else:
            index = len(self) - 1
        toPop = self._array[self._getArrayIndex(index)]
        self._array[self._getArrayIndex(index)] = None
        self._len -= 1
        if left:
            self._headIndex = (self._headIndex + 1) % len(self._array)
        return toPop

    def pop(self):
        return self._pop()

    def popLeft(self):
        return self._pop(left=True)
