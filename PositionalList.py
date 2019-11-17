class LinkedListDoubly:
    class Node:
        def __init__(self, item, nextNode, prevNode):
            self.item = item
            self.nextNode = nextNode
            self.prevNode = prevNode

    def __init__(self):
        self.header = self.Node(None, None, None)
        self.trailer = self.Node(None, None, None)
        self.header.nextNode = self.trailer
        self.trailer.prevNode = self.header
        self.length = 0

    def addNode(self, prev, next, item):
        result = prev.nextNode = next.prevNode = self.Node(item, next, prev)
        self.length += 1
        return result

    def removeNode(self, node):
        if self.length == 0:
            return None
        result = node.item
        node.prevNode.nextNode = node.nextNode
        node.nextNode.prevNode = node.prevNode
        self.length -= 1
        return result


class PositionalList(LinkedListDoubly):
    class Position:
        def __init__(self, node):
            self.node = node

    def __init__(self):
        super().__init__()

    def __str__(self):
        result, cur = [], self.header
        while cur.nextNode != self.trailer:
            cur = cur.nextNode
            result.append(cur.item)
        return str(result)

    def assignPosition(self, node):
        return self.Position(node)

    # UPDATE METHODS

    def addFirst(self, item):
        newNode = self.addNode(self.header, self.header.nextNode, item)
        return self.assignPosition(newNode)

    def addLast(self, item):
        newNode = self.addNode(self.trailer.prevNode, self.trailer, item)
        return self.assignPosition(newNode)

    def addBefore(self, position, item):
        newNode = self.addNode(position.node.prevNode, position.node, item)
        return self.assignPosition(newNode)

    def addAfter(self, position, item):
        newNode = self.addNode(position.node, position.node.nextNode, item)
        return self.assignPosition(newNode)

    def replace(self, position, item):
        prevItem = self.position.node.item
        self.position.node.item = item
        return prevItem

    def delete(self, position):
        result = position.node
        self.removeNode(position.node)
        return result

    # ACCESSOR METHODS

    def first(self):
        if self.length == 0:
            return None
        return self.assignPosition(self.header.nextNode)

    def last(self):
        if self.length == 0:
            return None
        return self.assignPosition(self.trailer.prevNode)

    def before(self, position):
        node = position.node.prevNode
        if node is self.header:
            return None
        else:
            return self.assignPosition(node)

    def after(self, position):
        node = position.node.nextNode
        if node is self.trailer:
            return None
        else:
            return self.assignPosition(node)

    def __iter__(self):
        pos = self.first()
        while pos is not None:
            yield pos
            pos = self.after(pos)

    def __len__(self):
        return self.length