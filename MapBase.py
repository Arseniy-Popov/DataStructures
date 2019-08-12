from collections import MutableMapping
from abc import abstractmethod


class MapBase(MutableMapping):
    class _Item:
        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __eq__(self, other):
            return self._key == other._key

        def __lt__(self, other):
            return self._key < other._key

        def __repr__(self):
            return f"({self._key}, {self._value})"
            

class HashMapBase(MapBase):
    def __init__(self):
        self._array = [None] * 10
        self._nItems = 0
        self._maxLoadFactor = 0.9

    def __len__(self):
        return self._nItems
    
    def _loadFactor(self):
        return self._nItems / len(self._array)

    def _compressionFunc(self, key, array=None):
        if array is None:
            array = self._array
        return hash(key) % len(array)

    def _resize(self):
        self._resizedArray = [None] * 2 * len(self._array)
        for key, value in self.items():
            self._set_bucket(key, value, array=self._resizedArray)
        self._array = self._resizedArray

    def __setitem__(self, key, value):
        self._nItems += 1
        if self._loadFactor() >= self._maxLoadFactor:
            self._resize()
        self._set_bucket(key, value)

    def __getitem__(self, key):
        return self._get_bucket(key)

    def __delitem__(self, key):
        self._del_bucket(key)

    @abstractmethod
    def _set_bucket(self, key, value, array=None):
        pass

    @abstractmethod
    def _get_bucket(self, key):
        pass

    @abstractmethod
    def _del_bucket(self, key):
        pass
