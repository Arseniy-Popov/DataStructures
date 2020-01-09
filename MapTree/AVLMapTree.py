from DataStructures.MapTree.MapTree import MapTree
import itertools as it


class AVLMapTree(MapTree):
    def _rebalance(self, position):
        walk = walk_1 = walk_2 = position
        while walk != self.root():
            walk, walk_1, walk_2 = self.parent(walk), walk, walk_1
            if self._heightDiff(walk) > 1:
                return self._trinodeRestructure(walk, walk_1, walk_2)

    def _trinodeRestructure(self, high, mid, low):
        if self._flagDoubleRotation(high, mid, low):
            mid, low = self._rotate(mid, low)
            self._rotate(high, mid)
        else:
            self._rotate(high, mid)

    def _rotate(self, upper, lower):
        subtrees = it.chain.from_iterable(self.children(p) for p in (upper, lower))
        subtrees = [s for s in subtrees if s not in (upper, lower)]
        # subtrees = [s for s in self._children(upper, lower) if s not in (upper, lower)]
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
        right_grandchild, left_grandchild = None, None
        if self.left(high) is not None and self.left(self.left(high)) is not None:
            left_grandchild = self.left(self.left(high)) == low
        if self.right(high) is not None and self.right(self.right(high)) is not None:
            right_grandchild = self.right(self.right(high)) == low
        if right_grandchild or left_grandchild:
            return False
        else:
            return True

    def _children(self, *positions):
        for position in positions:
            yield from self.children(position)

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
