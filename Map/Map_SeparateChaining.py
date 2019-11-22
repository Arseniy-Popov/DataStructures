from DataStructures.Map.MapBase import HashMapBase


class Map_SeparateChaining(HashMapBase):
    def __iter__(self):
        for a in self._array:
            if a is not None:
                for item in a:
                    yield item._key

    def _set_bucket(self, key, value):
        index = self._compressionFunc(key)
        if self._array[index] is None:
            self._array[index] = [self._Item(key, value)]
            self._nItems += 1
        else:
            for item in self._array[index]:
                if item._key == key:
                    item._value = value
                    return
            self._array[index].append(self._Item(key, value))
            self._nItems += 1

    def _get_bucket(self, key):
        index = self._compressionFunc(key)
        if self._array[index] is not None:
            for item in self._array[index]:
                if item._key == key:
                    return item._value
        raise KeyError(key)

    def _del_bucket(self, key):
        index = self._compressionFunc(key)
        if self._array[index] is not None:
            for innerIndex, item in enumerate(self._array[index]):
                if item._key == key:
                    del self._array[index][innerIndex]
                    self._nItems -= 1
                    return
        raise KeyError
