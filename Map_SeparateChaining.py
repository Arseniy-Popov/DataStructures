from Map.MapBase import HashMapBase


class Map_SeparateChaining(HashMapBase):
	def __iter__(self):
		for a in self._array:
			if a is not None:
				for item in a:
					yield item._key
	
	def _set_bucket(self, key, value, array=None):
		index = self._compressionFunc(key)
		if array[index] is None:
			array[index] = [self._Item(key, value)]
		else:
			for item in array[index]:
				if item._key == key:
					item._value = value
					return
			array[index].append(self._Item(key, value))

	def _get_bucket(self, key):
		index = self._compressionFunc(key)
		if self._array[index] is not None:
			for item in self._array[index]:
				if item._key == key:
					return item._value
		raise KeyError
	
	def _del_bucket(self, key):
		index = self._compressionFunc(key)
		if self._array[index] is not None:
			for item in self._array[index]:
				if item._key == key:
					self._array[index] = None
					return
		raise KeyError