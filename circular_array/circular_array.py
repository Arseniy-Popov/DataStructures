import collections.abc


class CircularArray(collections.abc.MutableSequence):
    """
    Array supporting constant time insertions and deletions
    on either end as well as constant time indexing.
    
    Insertions and deletions 
    
    Provides the .append, .appendLeft, .pop, .popLeft, __len__, __getitem__,
    __setitem__, __delitem__, and .insert methods by itself, and inherits
    __contains__, __iter__, __reversed__, .index, .count, .reverse, .extend,
    .remove, and __iadd__ from the collections.abc.MutableSequence abstract
    base class.
    """

    _initialSize = 10
    _resizeFactor = 2
    _shrinkThreshold = 0.5

    # Private utilities

    def _arrayIndex(self, index):
        """
        Get index of the underlying array corresponding to the
        perceived element index. Negative index points to the
        left of the _headIndex, not to the left of the end of
        the array.
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

    def _indexPositive(self, index):
        """
        Turns the negative index used to denote position
        relative to the end of the array into a positive one.
        """
        return index if index >= 0 else len(self) + index

    def _validate(self, index):
        """
        Validate the index is within the acceptable range.
        """
        if not 0 <= index < len(self):
            raise IndexError
        return index

    # Accessor methods

    def __len__(self):
        return self._len

    def __getitem__(self, index):
        index = self._validate(self._indexPositive(index))
        return self._array[self._arrayIndex(index)]

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
        index = self._validate(self._indexPositive(index))
        self._array[self._arrayIndex(index)] = value

    def _shift(self, fromIndex, toIndex):
        self._array[self._arrayIndex(fromIndex)] = self._array[
            self._arrayIndex(toIndex)
        ]

    def __delitem__(self, index):
        index = self._validate(self._indexPositive(index))
        if index < len(self) // 2:
            for i in range(index, 0, -1):
                self._shift(i-1, i)
            self._headIndex = (self._headIndex + 1) % len(self._array)
        else:
            for i in range(index, len(self)-1):
                self._shift(i+1, i)
        self._len -= 1
        self._resize()

    def insert(self, index, value):
        """
        Insert value before index.
        """
        self._resize()
        index = self._indexPositive(index)
        index = min(len(self), index)
        if index < len(self) // 2:
            for i in range(index):
                self._shift(i - 1, i)
            self._headIndex = (self._headIndex - 1) % len(self._array)
        else:
            for i in range(len(self) - 1, index - 1, -1):
                self._shift(i + 1, i)
        self._array[self._arrayIndex(index)] = value
        self._len += 1

    def append(self, value):
        """
        Append value to the end of the sequence.
        """
        self.insert(len(self), value)

    def appendLeft(self, value):
        """
        Append value to the front of the sequence.
        """
        self.insert(0, value)

    def pop(self, index=None):
        index = index or -1
        item = self[index]
        del self[-1]
        return item

    def popLeft(self):
        item = self[0]
        del self[0]
        return item
