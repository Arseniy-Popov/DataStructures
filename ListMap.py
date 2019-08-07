from Map.MapBase import MapBase


class ListMap(MapBase):
    def __init__(self):
        self._data = []
    
    def __iter__(self):
        for item in self._data:
            yield item._key
    
    def __len__(self):
        return len(self._data)
    
    def __setitem__(self, key, value):
        contains = False
        for item in self._data:
            if item._key == key:
                item._value = value
                contains = True
        if not contains:
            self._data.append(self._Item(key, value))
    
    def __getitem__(self, key):
        for item in self._data:
            if item._key == key:
                return item._value
        raise KeyError
    
    def __delitem__(self, key):
        contains = False
        for index, item in enumerate(self._data):
            if item._key == key:
                del self._data[index]
                contains = True
        if not contains:
            raise KeyError