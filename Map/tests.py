import unittest
from string import ascii_letters, ascii_lowercase
import random
from abc import ABC, abstractmethod

from DataStructures.Map.MapBase import HashMapBase
from DataStructures.Map.ListMap import ListMap
from DataStructures.Map.Map_SeparateChaining import Map_SeparateChaining
from DataStructures.Map.Map_LinearProbing import Map_LinearProbing
from DataStructures.Map.SortedListMap import SortedListMap


class TestMap_Base(ABC):
    @abstractmethod
    def initMap(self):
        self.map = None

    def initKeys(self):
        self.initial_keys = list(ascii_letters[::-1])

    def setUp(self):
        # random.seed(5)
        self.initMap()
        self.initKeys()
        self.test_dict = {}
        for index, key in enumerate(self.initial_keys):
            with self.subTest(key):
                self.map[key] = self.test_dict[key] = index ** 2

    def check_requirements(self):
        self.contents_match()

    def contents_match(self):
        for key in self.test_dict.keys():
            self.assertEqual(self.map[key], self.test_dict[key])

    def display_items(self):
        print(f"\n items:\n {list(self.map.items())}")

    def test_set_get(self):
        with self.subTest("initial"):
            self.contents_match()
        with self.subTest("reset"):
            for key in self.initial_keys:
                self.map[key] = self.test_dict[key] = -self.map[key]
            self.check_requirements()
        # self.display_items()

    def test_del(self):
        print(f"\ninitial_keys: \n{self.initial_keys}")
        self.initial_keys_post_deletion = self.initial_keys
        random.shuffle(self.initial_keys_post_deletion)
        print(f"deletion keys: \n{self.initial_keys_post_deletion}")
        deleted_keys = []
        while len(self.test_dict) > 1:
            key = self.initial_keys_post_deletion.pop(0)
            deleted_keys.append(key)
            del self.test_dict[key]
            del self.map[key]
            with self.subTest(key):
                self.check_requirements()
        self.assertRaises(KeyError, self.map.__getitem__, "c")
        self.assertRaises(KeyError, self.map.__delitem__, "c")

    def test_len(self):
        self.assertEqual(len(self.map), len(self.test_dict))


class TestMap_List(TestMap_Base, unittest.TestCase):
    def initMap(self):
        self.map = ListMap()


class TestMap_Hash_SeparateChaining(TestMap_List):
    def initMap(self):
        self.map = Map_SeparateChaining()

    # def test_container(self):
    #     print(f"\n container:\n {self.map._array}")


class TestMap_Hash_LinearProbing(TestMap_Hash_SeparateChaining):
    def initMap(self):
        self.map = Map_LinearProbing()


class TestMap_SortedListMap(TestMap_List):
    def initMap(self):
        self.map = SortedListMap()

    def test_lt(self):
        self.assertEqual(self.map.get_lt("J"), "I")

    def test_le(self):
        self.assertEqual(self.map.get_le("J"), "J")
        del self.map["a"]
        self.assertEqual(self.map.get_le("a"), "Z")


if __name__ == "__main__":
    # tests = []
    # # repeat line for each class
    # tests.append(unittest.TestLoader().loadTestsFromTestCase(TestMap_List))
    # suite = unittest.TestSuite(tests)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main(verbosity=2)
