from graphviz import Digraph
from abc import ABC, abstractmethod
from collections import deque


class Tree(ABC):
    class Position:
        def __init__(self, node, valid=True):
            self.node = node
            self.valid = valid

        def __eq__(self, other):
            return self.node == other.node

        def __ne__(self, other):
            return not self.__eq__(other)

    @abstractmethod
    def root(self):
        pass

    @abstractmethod
    def parent(self, position):
        pass

    @abstractmethod
    def numChildren(self, position):
        pass

    @abstractmethod
    def children(self, position):
        pass

    @abstractmethod
    def __len__(self):
        pass

    def positions(self):
        return self.traversePreorder()

    def traversePreorder(self, start=None):
        if start is None:
            start = self.root()
        yield start
        for i in self.children(start):
            yield from self.traversePreorder(start=i)

    def traversePostorder(self, start=None):
        if start is None:
            start = self.root()
        for i in self.children(start):
            yield from self.traversePostorder(start=i)
        yield start

    def traverseDFS(self, start=None):
        if start is None:
            start = self.root()
        queue = deque()
        queue.append(start)
        while len(queue) != 0:
            result = queue.popleft()
            yield result
            for i in self.children(result):
                queue.append(i)

    def isEmpty(self):
        return len(self) == 0

    def isRoot(self, position):
        return self.root() == position

    def isLeaf(self, position):
        return self.numChildren(position) == 0

    def depth(self, position):
        if self.isRoot(position):
            return 0
        else:
            return 1 + self.depth(self.parent(position))

    def heigth(self, position=None):
        if position is None:
            position = self.root()
        if self.isLeaf(position):
            return 1
        else:
            return 1 + max(self.heigth(p) for p in self.children(position))

    def graph(self):
        """Renders a graph using the Graphviz module."""
        graph = Digraph()
        graph.attr("node", shape="circle")
        for position in self.positions():
            graph.node(str(id(position.node)), label=str(position.node.item))
        for position in self.positions():
            for child in self.children(position):
                graph.edge(str(id(position.node)), str(id(child.node)))
        graph.render()


class BinaryTree(Tree):
    @abstractmethod
    def left(self, position):
        pass

    @abstractmethod
    def right(self, position):
        pass

    def sibling(self, position):
        if self.numChildren(self.parent(position)) == 1:
            return None
        elif self.left(self.parent(position)) == position:
            return self.right(self.parent(position))
        elif self.right(self.parent(position)) == position:
            return self.left(self.parent(position))

    def children(self, position):
        if self.right(position) is not None:
            yield self.right(position)
        if self.left(position) is not None:
            yield self.left(position)

    def traverseInorder(self, start=None):
        if start is None:
            start = self.root()
        if self.left(start) is not None:
            yield from self.traverseInorder(start=self.left(start))
        yield start
        if self.right(start) is not None:
            yield from self.traverseInorder(start=self.right(start))


class LinkedBinaryTree(BinaryTree):
    class Node:
        def __init__(self, parent, item, left=None, right=None):
            self.parent = parent
            self.left = left
            self.right = right
            self.item = item

    class Position(Tree.Position):
        def item(self):
            return self.node.item

    def __init__(self):
        self._root = None
        self.size = 0

    # MODIFIERS

    def addRoot(self, item):
        if self.size != 0:
            raise ValueError("non-empty tree")
        self._root = self.Node(None, item)
        self.size += 1
        return self.Position(self._root)

    def addLeft(self, position, item):
        position.node.left = self.Node(position.node, item)
        self.size += 1
        return self.Position(position.node.left)

    def addRight(self, position, item):
        position.node.right = self.Node(position.node, item)
        self.size += 1
        return self.Position(position.node.right)

    def replace(self, position, item):
        position.node.item == item

    def attach(self, position, tree1, tree2):
        if self.isLeaf(position) is not True:
            raise ValueError("node not a leaf")
        position.node.left = tree1.root().node
        position.node.right = tree2.root().node

    # ACCESORS

    def root(self):
        return self.Position(self._root)

    def parent(self, position):
        return self.Position(position.node.parent)

    def numChildren(self, position):
        return sum(1 for i in self.children(position))

    def children(self, position):
        if position.node.left is not None:
            yield self.Position(position.node.left)
        if position.node.right is not None:
            yield self.Position(position.node.right)

    def __len__(self):
        return self.size

    def left(self, position):
        if position.node.left is not None:
            return self.Position(position.node.left)
        else:
            return None

    def right(self, position):
        if position.node.right is not None:
            return self.Position(position.node.right)
        else:
            return None


def test():
    tree = LinkedBinaryTree()
    a = tree.addRoot("a")
    c = tree.addLeft(a, "c")
    d = tree.addRight(a, "d")
    tree.addRight(c, "f")
    g = tree.addLeft(c, "g")
    tree.addRight(d, "f")
    tree.addLeft(d, "g")
    tree.addLeft(g, "u")
    yield "traversals:"
    yield f"   preorder: \n      {' '.join(str(i.item()) for i in tree.traversePreorder())}"
    yield f"   postorder: \n      {' '.join(str(i.item()) for i in tree.traversePostorder())}"
    yield f"   inorder: \n      {' '.join(str(i.item()) for i in tree.traverseInorder())}"
    yield f"   DFS: \n      {' '.join(str(i.item()) for i in tree.traverseDFS())}"
    yield f"positions: {' '.join(str(i.item()) for i in tree.positions())}"
    yield f"heigth: {tree.heigth()}"
    yield f"len: {len(tree)}"
    tree.graph()


def testFilesystem():
    """leafs are files w/ file size and non-leafes are folders"""
    tree = LinkedBinaryTree()
    a = tree.addRoot(0)
    c = tree.addLeft(a, 0)
    d = tree.addRight(a, 0)
    tree.addRight(c, 5)
    g = tree.addLeft(c, 0)
    tree.addRight(d, 2)
    tree.addLeft(d, 4)
    tree.addLeft(g, 2)

    def sizeFilesystem(start=None):
        if start is None:
            start = tree.root()
        subtotal = 0
        for i in tree.children(start):
            subtotal += sizeFilesystem(start=i)
        subtotal += start.item()
        start.node.item = subtotal
        return subtotal

    yield sizeFilesystem()
    tree.graph()


if __name__ == "__main__":
    for i in testFilesystem():
        print(i)
