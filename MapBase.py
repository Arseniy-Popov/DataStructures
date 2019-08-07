from collections import MutableMapping

class MapBase(MutableMapping):
    class _Item:
        def __init__(self, key, value):
            self._key = key
            self._value = value
        
        def __eq__(self, other):
            return self._key == other._key
        
        def __lt__(self, other):
            return self._key < other._key


