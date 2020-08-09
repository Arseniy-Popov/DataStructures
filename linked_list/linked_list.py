import collections.abc


class LinkedList(collections.abc.Sequence):
    """
    Doubly linked list supporting constant time insertions
    and deletions at any location.    
    """

    class Node:
        def __init__(self, item, next=None, prev=None, container=None):
            self._next = next
            self._prev = prev
            self._container = container
            self.item = item

        def __repr__(self):
            return f"<Node {self.item}>"

        def _validateNode(self, node):
            if node == self._container._tail or node == self._container._head:
                return None
            return node

        def next(self):
            return self._validateNode(self._next)

        def prev(self):
            return self._validateNode(self._prev)

    # Modifier methods

    def __init__(self, iterable=None):
        self._head = self.Node(None, container=self)
        self._tail = self.Node(None, prev=self._head, container=self)
        self._head._next = self._tail
        self._len = 0
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def _link(self, preceding, following):
        preceding._next, following._prev = following, preceding

    def append(self, item, prev=None):
        """
        Insert item after the 'prev' node or to the end if no node is given.
        """
        prev = self._tail._prev if prev is None else prev
        new, next = self.Node(item, container=self), prev._next
        self._link(prev, new)
        self._link(new, next)
        self._len += 1

    def prepend(self, item, next=None):
        """
        Insert item before the 'next' node or to the front if no node is given.
        """
        next = self._head._next if next is None else next
        self.append(item, prev=next._prev)

    def delete(self, node):
        prev, next = node._prev, node._next
        self._link(prev, next)
        self._len -= 1
        return node

    # Accessor methods

    def __len__(self):
        return self._len

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError
        key = key if key >= 0 else len(self) + key
        if not 0 <= key <= len(self) - 1:
            raise IndexError
        if key > len(self) / 2:
            for count, node in enumerate(reversed(self)):
                if len(self) - count - 1 == key:
                    return node
        else:
            for count, node in enumerate(self):
                if count == key:
                    return node

    def _iter(self, direction, start):
        node = getattr(start, direction)()
        while node is not None:
            yield node
            node = getattr(node, direction)()

    def __iter__(self):
        return self._iter(start=self._head, direction="next")

    def __reversed__(self):
        return self._iter(start=self._tail, direction="prev")

    def __contains__(self, item):
        for node in self:
            if node.item == item:
                return True
        return False

    def __repr__(self):
        return f"<LinkedList {[node.item for node in self]}>"

    def index(self, item):
        for index, node in enumerate(self):
            if node.item == item:
                return index
        raise ValueError
