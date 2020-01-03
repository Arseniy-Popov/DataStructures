import unittest
import random
import shutil

from DataStructures.Map.tests import TestMap_Base
from DataStructures.MapTree.MapTree import MapTree
from DataStructures.MapTree.AVLMapTree import AVLMapTree


class Test_MapTree(TestMap_Base, unittest.TestCase):
    folder = "Output"

    @classmethod
    def setUpClass(cls):
        """Cleans up the output folder prior to the tests."""
        try:
            shutil.rmtree(cls.folder)
        except:
            pass

    def initMap(self):
        self.map = MapTree()

    def initKeys(self):
        self.initial_keys = random.sample(range(100), 20)

    def test_graph(self):
        self.map.graph(directory=Test_MapTree.folder)

    def test_iter(self):
        self.assertEqual(sorted(self.initial_keys), [i for i in self.map])


class Test_AVLMapTree(Test_MapTree):
    def initMap(self):
        self.map = AVLMapTree()


if __name__ == "__main__":
    unittest.main(verbosity=2)
