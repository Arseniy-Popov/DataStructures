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


class HashMapBase(MapBase):
    def __init__(self):
        self._array = [None] * 10
        self._arrayCapacity = len(self._array)
        self._nItems = 0

    def loadFactor(self):
        return self._nItems / self._arrayCapacity

    def compression(self, hash):
        return hash % self._arrayCapacity

    @abstractmethod
    def _insert_bucket(self, key):
        pass

    @abstractmethod
    def _get_bucket(self, key):
        pass

    @abstractmethod
    def _del_bucket(self, key):
        pass
