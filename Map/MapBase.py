from collections import MutableMapping
from abc import abstractmethod


class MapBase(MutableMapping):
    class _Item:
        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __eq__(self, other):
            return self._key == other._key

        def __repr__(self):
            return f"({self._key}, {self._value})"


class HashMapBase(MapBase):
    def __init__(self):
        self._array = [None] * 10
        self._nItems = 0
        self._maxLoadFactor = 0.6

    def __len__(self):
        return self._nItems

    def _loadFactor(self):
        return self._nItems / len(self._array)

    def _compressionFunc(self, key):
        return hash(key) % len(self._array)

    def _resize(self):
        items = list(self.items())
        self._array, self._nItems = [None] * 2 * len(self._array), 0
        for key, value in items:
            self[key] = value

    def __setitem__(self, key, value):
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
