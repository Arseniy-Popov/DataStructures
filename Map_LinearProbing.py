from Map.MapBase import HashMapBase


class Map_LinearProbing(HashMapBase):
    class _Empty:
        def __init__(self):
            """Array items that should not terminate search during linear probing."""
            pass

    def _set_bucket(self, key, value, array=None):
        if array is None:
            array = self._array
        startIndex = currentIndex = self._compressionFunc(key, array=array)
        add = 0
        while (
            array[currentIndex] is not None
            and not isinstance(array[currentIndex], self._Empty)
            and array[currentIndex]._key != key
        ):
            add += 1
            currentIndex = (startIndex + add) % len(array)
        array[currentIndex] = self._Item(key, value)

    def _findIndex(self, key):
        startIndex = currentIndex = self._compressionFunc(key)
        add = 0
        while self._array[currentIndex] is not None:
            if not isinstance(self._array[currentIndex], self._Empty):
                if self._array[currentIndex]._key == key:
                    return currentIndex
            add += 1
            currentIndex = (startIndex + add) % len(self._array)
        raise KeyError

    def _get_bucket(self, key):
        index = self._findIndex(key)
        return self._array[index]._value

    def __iter__(self):
        for item in self._array:
            if item is not None and not isinstance(item, self._Empty):
                yield item._key

    def _del_bucket(self, key):
        index = self._findIndex(key)
        self._array[index] = self._Empty()
