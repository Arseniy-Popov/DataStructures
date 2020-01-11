from DataStructures.Map.MapBase import MapBase
from DataStructures.Tree.Tree import LinkedBinaryTree


class MapTree(LinkedBinaryTree, MapBase):
    class Position(LinkedBinaryTree.Position):
        def key(self):
            return self.node.item._key

        def value(self):
            return self.node.item._value

    def _findKey(self, key, current, parent=None):
        if current is None:
            return parent
        if current.key() < key:
            return self._findKey(key, self.right(current), parent=current)
        elif current.key() > key:
            return self._findKey(key, self.left(current), parent=current)
        elif current.key() == key:
            return current

    def _rightmostInSubtree(self, position):
        """Returns position of the element with the largest key
        (the rightmost element) in a subtree."""
        while self.right(position) is not None:
            position = self.right(position)
        return position

    def _addLeaf(self, position, key, value):
        if position is None:
            added = self.addRoot(self._Item(key, value))
        elif position.key() < key:
            added = self.addRight(position, self._Item(key, value))
        else:
            added = self.addLeft(position, self._Item(key, value))
        return added

    def __getitem__(self, key):
        position = self._findKey(key, self.root())
        if position is not None and position.key() == key:
            return position.value()
        else:
            raise KeyError(f"key {key} not found")

    def __setitem__(self, key, value):
        position = self._findKey(key, self.root())
        if position is None or position.key() != key:
            size = len(self)
            added = self._addLeaf(position, key, value)
            self._rebalance(added)
            self.size = size + 1
        else:
            self.replace(position, self._Item(key, value))

    def __delitem__(self, key):
        position = self._findKey(key, self.root())
        if position is None or position.key() != key:
            raise KeyError
        if self.numChildren(position) <= 1:
            parent = self.parent(position)
            self.delete(position)
            self._rebalance(parent)
        else:
            replacement = self._rightmostInSubtree(self.left(position))
            self.replace(position, replacement.item())
            self.delete(replacement)

    def __iter__(self):
        yield from (i.key() for i in self.traverseInorder())

    def _rebalance(self, position):
        pass
