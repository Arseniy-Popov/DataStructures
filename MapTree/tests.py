import unittest
import random

from DataStructures.Map.tests import TestMap_Base
from DataStructures.MapTree.MapTree import MapTree


class Test_MapTree(TestMap_Base, unittest.TestCase):
    def initMap(self):
        self.map = MapTree()

    def initKeys(self):
        self.initial_keys = random.sample(range(100), 20)

    def test_graph(self):
        self.map.graph()

    def test_iter(self):
        self.assertEqual(sorted(self.initial_keys), [i for i in self.map])


if __name__ == "__main__":
    unittest.main(verbosity=2)
