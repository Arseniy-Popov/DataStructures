from DataStructures.MapTree.MapTree import MapTree


class AVLMapTree(MapTree):
    def _rebalance(self, position):
        walk = walk_1 = walk_2 = position
        while walk != self.root():
            walk, walk_1, walk_2 = self.parent(walk), walk, walk_1
            if self._heightDiff(walk) > 1:
                self._trinodeRestructure(walk, walk_1, walk_2)

    def _trinodeRestructure(self, z, x, y):
        subtrees, parent, isLeft = [], None, False
        a, b, c = sorted((z, x, y), key=lambda pos: pos.key())
        aItem, bItem, cItem = a.item(), b.item(), c.item()
        for position in a, b, c:
            for subtree in self.children(position):
                if subtree not in (a, b, c):
                    subtrees.append(subtree)
            if self.parent(position) not in (a, b, c):
                if self.parent(position) is None:
                    parent = None
                else:
                    if self.left(self.parent(position)) == position:
                        parent, isLeft = self.parent(position), True
                    else:
                        parent, isLeft = self.parent(position), False
        if parent is None:
            self.replace(self.root(), bItem)
            parent = self.root()
        else:
            if isLeft:
                parent = self.addLeft(parent, bItem)
            else:
                parent = self.addRight(parent, bItem)
        self.addLeft(parent, aItem)
        self.addRight(parent, cItem)
        self._trinodeRelinkSubtrees(parent, subtrees)

    def _trinodeRelinkSubtrees(self, trinode, subtrees):
        for subtree in subtrees:
            node = self._findKey(subtree.key(), trinode)
            if subtree.key() < node.key():
                self.relinkSubtree(node, subtree, left=True)
            else:
                self.relinkSubtree(node, subtree, left=False)

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
