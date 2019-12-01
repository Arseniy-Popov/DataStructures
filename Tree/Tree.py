from graphviz import Digraph
from abc import ABC, abstractmethod
from collections import deque
import datetime


class Tree(ABC):
    class Position:
        def __init__(self, node, valid=True):
            self.node = node

        def __eq__(self, other):
            if not isinstance(other, Tree.Position):
                return False
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

    @abstractmethod
    def delete(self, position):
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

    def traverseEuler(self, start=None):
        if start is None:
            start = self.root()
        yield start
        for i in self.children(start):
            yield from self.traverseEuler(i)
            yield start

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

    def height(self, position=None):
        if position is None:
            position = self.root()
        if self.isLeaf(position):
            return 1
        else:
            return 1 + max(self.heigth(p) for p in self.children(position))

    def graph(self, filename=None, directory="Output"):
        """Renders a graph using the Graphviz module."""
        graph = Digraph()
        graph.attr("node", shape="circle")
        for position in self.positions():
            graph.node(str(id(position.node)), label=str(position.node.item))
        for position in self.positions():
            for child in self.children(position):
                graph.edge(str(id(position.node)), str(id(child.node)))
        if filename is None:
            graph.render(filename=str(datetime.datetime.utcnow()), directory=directory)
        else:
            graph.render(filename=filename, directory=directory)


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

    def validatePosition(self):
        pass

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

    def delete(self, position):
        """Delete a node with a single leaf
        and replace it with its child."""
        if self.numChildren(position) > 1:
            raise ValueError
        elif self.numChildren(position) == 0:
            if position != self.root():
                if self.left(self.parent(position)) == position:
                    self.parent(position).node.left = None
                else:
                    self.parent(position).node.right = None
            else:
                self._root = None
            position.node.parent = position.node
        else:
            parent, child = self.parent(position), next(self.children(position))
            if self.left(parent) == position:
                parent.node.left = child.node
            else:
                parent.node.right = child.node
            child.node.parent = parent.node
            position.node.parent = position.node
        self.size -= 1

    # ACCESORS

    def root(self):
        if self._root is None:
            return None
        return self.Position(self._root)

    def parent(self, position):
        if position.node.parent is None:
            return None
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
