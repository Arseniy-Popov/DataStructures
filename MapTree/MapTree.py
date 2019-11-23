from DataStructures.Map.MapBase import MapBase
from DataStructures.Tree import LinkedBinaryTree


class MapTree(MapBase, LinkedBinaryTree):
    def _findKey(self, key, current, parent=None):
        if current is None:
            return parent
        if current.item._key < key:
            self._findKey(key, self.right(current), parent=current)
        elif current.item._key > key:
            self._findKey(key, self.left(current), parent=current)
        elif current.item._key == key:
            return current
    
    def __getitem__(self, key):
        position = self._findKey(key, self.root())
        if position is None or position.item._key == key:
            return position.item._value
        else:
            raise ValueError('key not found')
    
    def __setitem__(self, key, value):
        position = self._findKey(key, self.root())
        if position is None:
            self.addRoot(self._Item(key, value))
        elif position.item._key != key:
            if position.item._key < key:
                self.addRight(position, self._Item(key, value))
            else:
                self.addLeft(position, self._Item(key, value))
        else:
            position.item._value = value