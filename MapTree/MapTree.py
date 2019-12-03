from DataStructures.Map.MapBase import MapBase
from DataStructures.Tree.Tree import LinkedBinaryTree


class MapTree(LinkedBinaryTree, MapBase):
    def _findKey(self, key, current, parent=None):
        if current is None:
            return parent
        if current.item()._key < key:
            return self._findKey(key, self.right(current), parent=current)
        elif current.item()._key > key:
            return self._findKey(key, self.left(current), parent=current)
        elif current.item()._key == key:
            return current

    def _rightmostInSubtree(self, position):
        """Returns position of the element with the largest key
        (the rightmost element) in a subtree."""
        if self.right(position) is not None:
            return self._rightmostInSubtree(self.right(position))
        else:
            return position

    def __getitem__(self, key):
        position = self._findKey(key, self.root())
        if position is not None and position.item()._key == key:
            return position.item()._value
        else:
            raise KeyError(f"key {key} not found")

    def __setitem__(self, key, value):
        position = self._findKey(key, self.root())
        if position is None:
            self.addRoot(self._Item(key, value))
        elif position.item()._key != key:
            if position.item()._key < key:
                self.addRight(position, self._Item(key, value))
            else:
                self.addLeft(position, self._Item(key, value))
        else:
            position.item()._value = value

    def __delitem__(self, key):
        position = self._findKey(key, self.root())
        if self.numChildren(position) <= 1:
            self.delete(position)
        else:
            replacement = self._rightmostInSubtree(self.left(position))
            self.replace(position, replacement.item())
            self.delete(replacement)

    def __iter__(self):
        yield from (i.item()._key for i in self.traverseInorder())
