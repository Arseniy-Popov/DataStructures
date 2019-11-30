import unittest
from DataStructures.Tree.Tree import LinkedBinaryTree
from DataStructures.Tree.toc import tOfContents


class test_BinaryTree(unittest.TestCase):
    def setUp(self):
        self.tree = LinkedBinaryTree()
        a = self.tree.addRoot("a")
        c = self.tree.addLeft(a, "c")
        d = self.tree.addRight(a, "d")
        self.tree.addRight(c, "f")
        g = self.tree.addLeft(c, "g")
        self.tree.addRight(d, "f")
        self.tree.addLeft(d, "g")
        self.tree.addLeft(g, "u")
        h = self.tree.addRight(g, "y")
        self.tree.addRight(h, "z")
        self.tree.graph()

    def traversal_to_items(self, iterable):
        return [position.item() for position in iterable]

    def test_root(self):
        self.assertEqual(self.tree.root().item(), "a")

    def test_del(self):
        self.tree.delete(h)

    def test_traversals(self):
        print("\n")
        print(f"preorder: {self.traversal_to_items(self.tree.traversePreorder())}")
        print(f"postorder: {self.traversal_to_items(self.tree.traversePostorder())}")
        print(f"inorder: {self.traversal_to_items(self.tree.traverseInorder())}")
        print(f"DFS: {self.traversal_to_items(self.tree.traverseDFS())}")
        print(f"Euler: {self.traversal_to_items(self.tree.traverseEuler())}")


class test_toc(unittest.TestCase):
    def setUp(self):
        self.tree = LinkedBinaryTree()
        a = self.tree.addRoot("Book")
        b = self.tree.addLeft(a, "Part")
        c = self.tree.addRight(a, "Part")
        self.tree.addLeft(b, "Section")
        d = self.tree.addRight(b, "Section")
        self.tree.addLeft(c, "Section")
        self.tree.addLeft(d, "Sub-Section")
        self.tree.addRight(d, "Sub-Section")
        self.tree.graph(filename="toc")

    def test_typeOfArgumentTOC(self):
        self.assertRaises(ValueError, tOfContents, [])

    def test_toc(self):
        print("\n")
        tOfContents(self.tree)


if __name__ == "__main__":
    unittest.main(verbosity=2)
