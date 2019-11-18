from Tree.Tree import LinkedBinaryTree


def tOfContents(tree):
    def _tOfContents(tree, position=None, depth=0, parentString="", count=0):
        if not isinstance(tree, LinkedBinaryTree):
            raise ValueError("unsupported object as tree")
        if position is None:
            position = tree.root()
        count = 0
        for child in tree.children(position):
            count += 1
            string = parentString + str(count) + "."
            print(" " * depth, string, position.item())
            _tOfContents(
                tree, position=child, depth=depth + 1, parentString=string, count=count
            )

    return _tOfContents(tree)
