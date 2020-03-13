from DataStructures.MapTree.MapTree import MapTree
import itertools as it


class AVLMapTree(MapTree):
    class _Item(MapTree._Item):
        def __init__(self, key, value):
            super().__init__(key, value)
            self._height = 0
        
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
        if self._flagDoubleRotation(high, mid, low):
            mid, low = self._rotate(mid, low)
            high, mid = self._rotate(high, mid)
            self._recalcHeight(low, mid, high)
        else:
            high, mid = self._rotate(high, mid)
            self._recalcHeight(mid, high)

    def _rotate(self, upper, lower):
        subtrees = it.chain.from_iterable(self.children(p) for p in (upper, lower))
        subtrees = [s for s in subtrees if s not in (upper, lower)]
        new_upper = self._addLeaf(self.parent(upper), lower.key(), lower.value())
        new_lower = self._addLeaf(new_upper, upper.key(), upper.value())
        self._relinkSubtrees(new_upper, subtrees)
        return new_upper, new_lower

    def _relinkSubtrees(self, start, subtrees):
        for subtree in subtrees:
            node = self._findKey(subtree.key(), start)
            if subtree.key() < node.key():
                self.relinkSubtree(node, subtree, left=True)
            else:
                self.relinkSubtree(node, subtree, left=False)

    def _flagDoubleRotation(self, high, mid, low):
        """ Single rotation if low is either left of left 
        of high or right of right of high, double rotation otherwise. """
        try:  # check if left of left
            flag_left = self.left(self.left(high)) == low
        except:
            flag_left = False
        try:  # check if right of right
            flag_right = self.right(self.right(high)) == low
        except:
            flag_right = False
        if flag_left or flag_right:  # check if either
            return False
        else:
            return True

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
