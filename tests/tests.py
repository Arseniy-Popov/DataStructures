import unittest
from Tree.Tree import LinkedBinaryTree


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
        self.tree.graph()
    
    def test_root(self):
        self.assertEqual(self.tree.root().item(), "a")
    
    

if __name__ == "__main__":
    unittest.main()