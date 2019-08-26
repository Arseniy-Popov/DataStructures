import unittest
from string import ascii_letters, ascii_lowercase

from Map.MapBase import HashMapBase
from Map.ListMap import ListMap
from Map.Map_SeparateChaining import Map_SeparateChaining
from Map.Map_LinearProbing import Map_LinearProbing
from Map.SortedListMap import SortedListMap


class TestMap_List(unittest.TestCase):
    def initMap(self):
        self.map = ListMap()

    def setUp(self):
        self.initMap()
        self.initial_keys = ascii_letters
        for index, letter in enumerate(self.initial_keys):
            self.map[letter] = index
        self.deleted_Keys = ascii_lowercase
        self.remaining_Keys = "".join(
            [i for i in self.initial_keys if i not in self.deleted_Keys]
        )
        for key in self.deleted_Keys:
            del self.map[key]
        for key in self.remaining_Keys:
            self.map[key] = self.initial_keys.index(key) ** 2

    def test_set_get(self):
        for key in self.remaining_Keys:
            self.assertEqual(self.map[key], self.initial_keys.index(key) ** 2)
        self.map["d"] = 4
        self.assertEqual(self.map["d"], 4)

    def test_del(self):
        self.assertRaises(KeyError, self.map.__getitem__, "c")

    def test_len(self):
        self.assertEqual(len(self.map), len(self.remaining_Keys))

    def test_items(self):
        print(f"\n items:\n {list(self.map.items())}")


class TestMap_Hash_SeparateChaining(TestMap_List):
    def initMap(self):
        self.map = Map_SeparateChaining()

    def test_container(self):
        print(f"\n container:\n {self.map._array}")


class TestMap_Hash_LinearProbing(TestMap_Hash_SeparateChaining):
    def initMap(self):
        self.map = Map_LinearProbing()


class TestMap_SortedListMap(TestMap_List):
    def initMap(self):
        self.map = SortedListMap()


if __name__ == "__main__":
    tests = []
    # repeat line for each class
    tests.append(
        unittest.TestLoader().loadTestsFromTestCase(TestMap_SortedListMap)
    )
    suite = unittest.TestSuite(tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main(verbosity=2)
