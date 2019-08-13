import unittest

from Map.MapBase import HashMapBase
from Map.ListMap import ListMap
from Map.Map_SeparateChaining import Map_SeparateChaining
from Map.Map_LinearProbing import Map_LinearProbing


class TestMap_List(unittest.TestCase):
    def initMap(self):
        self.map = ListMap()

    def setUp(self):
        self.initMap()
        self.keys = "abcdefghijklm"
        for index, letter in enumerate(self.keys):
            self.map[letter] = index

    def test_set_get(self):
        self.assertEqual(self.map["a"], 0)
        self.map["d"] = 4
        self.assertEqual(self.map["d"], 4)
        self.assertEqual(self.map["m"], 12)

    def test_del(self):
        del self.map["c"]
        self.assertRaises(KeyError, self.map.__getitem__, "c")

    def test_iter(self):
        self.assertEqual(set([key for key in self.map]), set(self.keys))

    def test_len(self):
        self.assertEqual(len(self.map), 13)

    def test_keys(self):
        self.assertEqual(set(self.map.keys()), set(self.keys))

    def test_items(self):
        print(f"\n items: {list(self.map.items())}")


class TestMap_Hash_SeparateChaining(TestMap_List):
    def initMap(self):
        self.map = Map_SeparateChaining()

    def test_container(self):
        print(f"\n {self.map._array}")


class TestMap_Hash_LinearProbing(TestMap_Hash_SeparateChaining):
    def initMap(self):
        self.map = Map_LinearProbing()


if __name__ == "__main__":
    tests = []
    # repeat line for each class
    tests.append(
        unittest.TestLoader().loadTestsFromTestCase(TestMap_Hash_LinearProbing)
    )
    suite = unittest.TestSuite(tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main(verbosity=2)
