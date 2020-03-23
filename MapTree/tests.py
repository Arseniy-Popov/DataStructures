import unittest
import random
import shutil
import time

from DataStructures.Map.tests import TestMap_Base
from DataStructures.Map.Map_LinearProbing import Map_LinearProbing
from DataStructures.Map.Map_SeparateChaining import Map_SeparateChaining
from DataStructures.MapTree.MapTree import MapTree
from DataStructures.MapTree.AVLMapTree import AVLMapTree
from DataStructures.Tree.Tree import Tree


class Test_MapTree(TestMap_Base, unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Cleans up the output folder prior to the tests."""
        cls.folder = f"Output"
        cls.subfolder = cls.folder + f"/{cls.__name__}"
        try:
            shutil.rmtree(cls.subfolder)
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

    def test_del(self):
        print(f"\ninitial_keys: \n{self.initial_keys}")
        self.initial_keys_post_deletion = self.initial_keys
        random.shuffle(self.initial_keys_post_deletion)
        print(f"deletion keys: \n{self.initial_keys_post_deletion}")
        deleted_keys = []
        while len(self.test_dict) > 1:
            key = self.initial_keys_post_deletion.pop(0)
            deleted_keys.append(key)
            self.map.graph(
                filename=f"del {key}", directory=f"Output/{self.__class__.__name__}"
            )
            del self.test_dict[key]
            del self.map[key]
            with self.subTest(key):
                self.check_requirements()


class Test_AVLMapTree(Test_MapTree):
    def initMap(self):
        self.map = AVLMapTree()

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

    # def test_trinode_restructures(self):
    #     self.initMap()
    #     self.test_dict, previous = {}, None
    #     data = (30, 20, 40, 10, 25, 35, 50, 5, 15, 45, 55)
    #     for key in data:
    #         self.map[key] = 0
    #     test_cases = {
    #         "double_right": self.map.root(), self.map.root().right(), self.map.root().right().right)
    #     {
    #     for case in test_cases:
    #         for key in self.test_cases:
    #             self.map[key] = self.test_dict[key] = 0

    def test_buildup(self):
        print(f"\ninitial_keys: {self.initial_keys}")
        self.initMap()
        self.test_dict, previous = {}, None
        for index, key in enumerate(self.initial_keys):
            with self.subTest(key=key, previous=previous):
                self.map[key] = self.test_dict[key] = index ** 2
                self.check_requirements()
            previous = key
            self.map.graph(filename=str(key), directory=self.subfolder)

    def test_balanced(self):
        self.assertLessEqual(
            max(self._test_heightDiff(self.map, p) for p in self.map.positions()), 1
        )

    def check_requirements(self):
        self.contents_match()
        self.test_balanced()

    def test_speed(self):
        data_structures = [
            Map_LinearProbing,
            Map_SeparateChaining,
            dict,
            MapTree,
            AVLMapTree,
        ]
        # keys = range(5000)
        keys = random.sample(range(1000), 1000)
        for data_structure in data_structures:
            startTime = time.time()
            map = data_structure()
            for key in keys:
                map[key] = 0
            for key in keys:
                map[key]
            # for key in keys:
            #     del map[key]
            endTime = time.time()
            elapsedTime = endTime - startTime
            print(f"\n{data_structure}: \n{elapsedTime}")
            # if data_structure is AVLMapTree:
            #     map.graph()

    # height

    def _test_heightDiff(self, map, position):
        return abs(
            self._test_rightHeight(map, position) - self._test_leftHeight(map, position)
        )

    def _test_rightHeight(self, map, position):
        if map.right(position) is None:
            return 0
        else:
            return self._test_height(map, map.right(position))

    def _test_leftHeight(self, map, position):
        if map.left(position) is None:
            return 0
        else:
            return self._test_height(map, map.left(position))

    def _test_height(self, map, position):
        return Tree.height(map, position)


if __name__ == "__main__":
    unittest.main(verbosity=2)
