from collections.abc import Container, Sized


class LinkedList(Container, Sized):
    """
    Doubly linked list supporting constant time insertions
    and deletions at any location.
    
    Mosth of the methods accepts and/or return instances of
    LinkedList.Node, although __contains__ and .index
    accept items which should be contained at nodes.
    
    Internally, two sentinel nodes, _head and _tail, are 
    always present to simplify operations at endpoints,
    though this is not revealed to the user.
    """

    class Node:
        """
        Contained item is at .item. The node should not be 
        initailized by itself. Instead, use the appripriate
        modifying method of the LinkedList. 
        """
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
            """
            Returns the next node or None.
            """
            return self._validateNode(self._next)

        def prev(self):
            """
            Returns the previous node or None.
            """
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

    def append(self, item, prev=None) -> None:
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
        """
        Delete node.
        """
        prev, next = node._prev, node._next
        self._link(prev, next)
        self._len -= 1
        return node

    # Accessor methods

    def __len__(self):
        return self._len

    def __getitem__(self, index):
        """
        Returns node at given index.
        """
        if not isinstance(index, int):
            raise TypeError
        index = index if index >= 0 else len(self) + index
        if not 0 <= index <= len(self) - 1:
            raise IndexError
        if index > len(self) / 2:
            for count, node in enumerate(reversed(self)):
                if len(self) - count - 1 == index:
                    return node
        else:
            for count, node in enumerate(self):
                if count == index:
                    return node

    def _iter(self, direction, start):
        node = getattr(start, direction)()
        while node is not None:
            yield node
            node = getattr(node, direction)()

    def __iter__(self):
        """
        Iterate over the nodes of the list.
        """
        return self._iter(start=self._head, direction="next")

    def __reversed__(self):
        """
        Iterate over the nodes of the list in reverse.
        """
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
