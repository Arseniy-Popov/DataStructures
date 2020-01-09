import unittest
import random
import shutil

from DataStructures.Map.tests import TestMap_Base
from DataStructures.MapTree.MapTree import MapTree
from DataStructures.MapTree.AVLMapTree import AVLMapTree


class Test_MapTree(TestMap_Base, unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Cleans up the output folder prior to the tests."""
        cls.folder = f"Output"
        cls.subfolder = cls.folder + f"/{cls.__name__}"
        try:
            shutil.rmtree(cls.folder)
        except:
            pass

    def initMap(self):
        self.map = MapTree()

    def initKeys(self):
        self.initial_keys = random.sample(range(100), 20)

    def test_graph(self):
        self.map.graph(directory=self.subfolder)

    def test_iter(self):
        self.assertEqual(sorted(self.initial_keys), [i for i in self.map])


class Test_AVLMapTree(Test_MapTree):
    def initMap(self):
        self.map = AVLMapTree()

    def setUp(self):
        pass

    def test_rotations(self):
        self.test_cases = {
            "single_left": (5, 4, 3),
            "single_right": (1, 4, 6),
            "double_right": (10, 20, 15),
            "double_left": (10, 5, 8),
        }
        for case in self.test_cases:
            self.initMap()
            self.test_dict, previous = {}, None
            for key in self.test_cases[case]:
                with self.subTest(case=case, key=key, previous=previous):
                    self.map[key] = self.test_dict[key] = random.randint(1, 10)
                    self.contents_match()
                previous = key
            self.map.graph(filename=f"{case}", directory=self.subfolder)

    def test_buildup(self):
        # random.seed(5)
        self.initKeys()
        print(f"\n initial_keys: {self.initial_keys}")
        self.initMap()
        self.test_dict, previous = {}, None
        for index, key in enumerate(self.initial_keys):
            with self.subTest(key=key, previous=previous):
                self.map[key] = self.test_dict[key] = index ** 2
                self.contents_match()
            previous = key
            self.map.graph(filename=str(key), directory=self.subfolder)


if __name__ == "__main__":
    unittest.main(verbosity=2)
