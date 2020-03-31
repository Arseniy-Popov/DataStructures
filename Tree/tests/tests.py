import shutil
import unittest

from DataStructures.Tree.toc import tOfContents
from DataStructures.Tree.Tree import LinkedBinaryTree


class test_BinaryTree(unittest.TestCase):
    folder = "Output"

    @classmethod
    def setUpClass(cls):
        """Cleans up the output folder prior to the tests."""
        try:
            shutil.rmtree(cls.folder)
        except:
            pass

    def setUp(self):
        self.tree = LinkedBinaryTree()
        self.a = self.tree.addRoot("a")
        self.c = self.tree.addLeft(self.a, "c")
        self.d = self.tree.addRight(self.a, "d")
        self.tree.addRight(self.c, "f")
        self.g = self.tree.addLeft(self.c, "g")
        self.f = self.tree.addRight(self.d, "f")
        self.t = self.tree.addLeft(self.d, "t")
        self.tree.addLeft(self.g, "u")
        self.h = self.tree.addRight(self.g, "y")
        self.tree.addRight(self.h, "z")

    def traversal_to_items(self, iterable):
        return [position.item() for position in iterable]

    def test_root(self):
        self.assertEqual(self.tree.root().item(), "a")

    def test_relink_subtree(self):
        self.tree.relinkSubtree(self.t, self.g)
        self.tree.graph(filename="relink")

    def test_del(self):
        self.tree.graph(filename="initial")
        self.tree.delete(self.h)
        self.tree.graph(filename="deletion")

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
