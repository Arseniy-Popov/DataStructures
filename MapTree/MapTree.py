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
    
    def __setitem__(self, key, value):
        