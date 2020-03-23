from DataStructures.MapTree.MapTree import MapTree
import itertools as it


class AVLMapTree(MapTree):
    class _Item(MapTree._Item):
        def __init__(self, key, value):
            super().__init__(key, value)
            self._height = 1

        def __repr__(self):
            return f"({self._key}, {self._value}, {self._height})"

    def _rebalanceSet(self, position):
        walk = walk_1 = walk_2 = position
        while walk != self.root():
            walk, walk_1, walk_2 = self.parent(walk), walk, walk_1
            self._recalcHeight(walk)
            if self._heightDiff(walk) > 1:
                return self._trinodeRestructure(walk, walk_1, walk_2)

    def _rebalanceDel(self, position):
        while position is not None:
            self._recalcHeight(position)
            if self._heightDiff(position) > 1:
                low = mid = high = position
                while mid == high:
                    if self._rightHeight(low) >= self._leftHeight(low):
                        low, mid, high = self.right(low), low, mid
                    else:
                        low, mid, high = self.left(low), low, mid
                self._trinodeRestructure(high, mid, low)
            position = self.parent(position)

    def _trinodeRestructure(self, high, mid, low):
        if (self.right(mid) == low) == (self.right(high) == mid):
            high, mid = self._rotate(high, mid)
            self._recalcHeight(mid, high)
        else:
            mid, low = self._rotate(mid, low)
            high, mid = self._rotate(high, mid)
            self._recalcHeight(low, mid, high)

    def _rotate(self, upper, lower):
        lowerIsLeft = self.left(upper) == lower
        if self.isRoot(upper):
            self.relinkSubtree(None, lower)
        else:
            upperIsLeft = self.left(self.parent(upper)) == upper
            self.relinkSubtree(self.parent(upper), lower, left=upperIsLeft)
        if lowerIsLeft:
            self.relinkSubtree(upper, self.right(lower), left=True)
        else:
            self.relinkSubtree(upper, self.left(lower), left=False)
        self.relinkSubtree(lower, upper, left=(not lowerIsLeft))
        return lower, upper

    def _relinkSubtrees(self, start, subtrees):
        for subtree in subtrees:
            node = self._findKey(subtree.key(), start)
            if subtree.key() < node.key():
                self.relinkSubtree(node, subtree, left=True)
            else:
                self.relinkSubtree(node, subtree, left=False)

    def _recalcHeight(self, *positions):
        for position in positions:
            position.node.item._height = 1 + max(
                self._rightHeight(position), self._leftHeight(position)
            )

    def height(self, position):
        return position.node.item._height

    def _heightDiff(self, position):
        return abs(self._rightHeight(position) - self._leftHeight(position))

    def _rightHeight(self, position):
        if self.right(position) is None:
            return 0
        else:
            return self.height(self.right(position))

    def _leftHeight(self, position):
        if self.left(position) is None:
            return 0
        else:
            return self.height(self.left(position))
