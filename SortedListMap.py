from Map.MapBase import MapBase


class SortedListMap(MapBase):
    def __init__(self):
        self._data = []
    
    def _binarySearch(self, key, low=None, high=None):
        if low is None and high is None:
            low, high = 0, len(self._data) - 1
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
        
    def __getitem__(self, key):
        foundKey, index = self._binarySearch(key)
        if not foundKey:
            raise KeyError
        else:
            return self._data[index]._value
    
    def __delitem__(self, key):
        foundKey, index = self._binarySearch(key)
        if not foundKey:
            raise KeyError
        else:
            del self._data[index]
    
    def __iter__(self):
        for item in self._data:
            yield item._value
    
    def __len__(self):
        return len(self._data)