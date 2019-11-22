from DataStructures.Map.MapBase import MapBase


class SortedListMap(MapBase):
    """ Map with keys sorted in ascending order.
    
    TODO: get_ methods besides le, lt """

    def __init__(self):
        self._data = []

    def __iter__(self):
        for item in self._data:
            yield item._key

    def __len__(self):
        return len(self._data)

    def _binarySearch(self, key, low=None, high=None):
        if low is None and high is None:
            low, high = 0, len(self._data) - 1
        if high < low:
            return high + 1
        mid = (high + low) // 2
        if self._data[mid]._key == key:
            return mid
        elif self._data[mid]._key > key:
            return self._binarySearch(key, low=low, high=mid - 1)
        elif self._data[mid]._key < key:
            return self._binarySearch(key, low=mid + 1, high=high)

    def __setitem__(self, key, value):
        index = self._binarySearch(key)
        if index > len(self) - 1:
            self._data.append(self._Item(key, value))
        elif self._data[index]._key == key:
            self._data[index]._value = value
        else:
            self._data.insert(index, self._Item(key, value))

    def __getitem__(self, key):
        index = self._binarySearch(key)
        if index > len(self) - 1 or self._data[index]._key != key:
            raise KeyError
        else:
            return self._data[index]._value

    def __delitem__(self, key):
        index = self._binarySearch(key)
        if index > len(self) - 1 or self._data[index]._key != key:
            raise KeyError
        else:
            del self._data[index]

    def get_lt(self, key):
        index = self._binarySearch(key)
        if index - 1 >= 0:
            return self._data[index - 1]._key
        else:
            raise KeyError

    def get_le(self, key):
        index = self._binarySearch(key)
        if not index > len(self) - 1 and self._data[index]._key == key:
            return self._data[index]._key
        elif index - 1 >= 0:
            return self._data[index - 1]._key
        else:
            raise KeyError
