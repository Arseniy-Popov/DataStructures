from Map.MapBase import HashMapBase


class Map_LinearProbing(HashMapBase):
    class _Empty:
        def __init__(self):
            """Array items that should not terminate search during linear probing."""
            pass

        def __repr__(self):
            return "_Empty"

    def _findIndex(self, key):
        startIndex = currentIndex = self._compressionFunc(key)
        add, emptyIndex = 0, None
        while True:
            if (
                isinstance(self._array[currentIndex], self._Empty)
                or self._array[currentIndex] is None
            ):
                if emptyIndex is None:
                    emptyIndex = currentIndex
                if self._array[currentIndex] is None:
                    return (False, emptyIndex)
            elif self._array[currentIndex]._key == key:
                return (True, currentIndex)
            add += 1
            currentIndex = (startIndex + add) % len(self._array)

    def _set_bucket(self, key, value):
        foundKey, index = self._findIndex(key)
        self._array[index] = self._Item(key, value)
        if not foundKey:
            self._nItems += 1

    def _get_bucket(self, key):
        foundKey, index = self._findIndex(key)
        if foundKey:
            return self._array[index]._value
        else:
            raise KeyError

    def _del_bucket(self, key):
        foundKey, index = self._findIndex(key)
        if foundKey:
            self._array[index] = self._Empty()
            self._nItems -= 1
        else:
            raise KeyError

    def __iter__(self):
        for item in self._array:
            if item is not None and not isinstance(item, self._Empty):
                yield item._key
