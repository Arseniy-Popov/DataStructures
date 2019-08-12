import unittest


from Map.MapBase import HashMapBase
from Map.ListMap import ListMap
from Map.Map_SeparateChaining import Map_SeparateChaining


class TestMap_List(unittest.TestCase):
    def initMap(self):
        self.map = ListMap()
    
    def setUp(self):
        self.initMap()
        self.map["a"] = 1
        self.map["b"] = 2
        self.map["c"] = 3

    def test_set_get(self):
        self.assertEqual(self.map["a"], 1)
        self.map["d"] = 4
        self.assertEqual(self.map["d"], 4)

    def test_del(self):
        del self.map["c"]
        self.assertRaises(KeyError, self.map.__getitem__, "c")

    def test_iter(self):
        self.assertEqual(set([key for key in self.map]), set(["a", "b", "c"]))

    def test_len(self):
        self.assertEqual(len(self.map), 3)

    def test_keys(self):
        self.assertEqual(set(self.map.keys()), set(["a", "b", "c"]))

    def test_items(self):
        print(f"\n items: {list(self.map.items())}")


class TestMap_Hash_SeparateChaining(TestMap_List):
    def initMap(self):
        self.map = Map_SeparateChaining()

    def test_container(self):
        print(f"\n {self.map._array}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
