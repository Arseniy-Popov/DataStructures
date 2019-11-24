import unittest 

from DataStructures.Map.tests import TestMap_Base
from DataStructures.MapTree.MapTree import MapTree


class Test_MapTree(TestMap_Base, unittest.TestCase):
    def initMap(self):
        self.map = MapTree()


if __name__ == "__main__":
    unittest.main(verbosity=2)
