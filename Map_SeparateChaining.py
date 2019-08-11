from Map.MapBase import HashMapBase


class Map_SeparateChaining(HashMapBase):
    def _set_bucket(self, key, value, array=None):
        index = self._compressionFunc(key)
        if self._array[index] is None:
            self._array[index] = [self._Item(key, value)]
        else:
            for item in self._array[index]:
                if item._key == key:
                    item._value = value
                    return
            self._array[index].append(self._Item(key, value))

    def _get_bucket(self, key):
