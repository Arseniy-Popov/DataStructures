from Map.MapBase import MapBase


class SortedListMap(MapBase):
    def __init__(self):
        self._data = []
        self._nItems = 0
    
    def _bisectionSearch(self, key, low=None, high=None):
        if low is None and high is None:
            low, high = 0, self._nItems - 1
        if high == low and self._data[low]._key != key:
            if self._data[low]._key > key:
                return (False, low)
        mid = (high + low) // 2
        if self._data[mid]._key == key:
            return (True, mid)
        if self._data[mid]._key > key:
            self._bisectionSearch(key, low=low, high=mid-1)
        else:
            self._bisectionSearch(key, low=mid+1, high=high)
    
    def __setitem__(self, key, value):
        foundKey, index = self._binarySearch(key)
        if foundKey:
            self._data[index]._value == value
        else:
            if key < self._data[index]._key:
                self._data.insert(index, self._Item(key, value))
            else:
                self._data.insert(index+1, self._Item(key, value))
        
        