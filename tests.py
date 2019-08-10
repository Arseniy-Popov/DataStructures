import unittest


from Map.MapBase import HashMapBase
from Map.ListMap import ListMap


class TestListMap(unittest.TestCase):
    def setUp(self):
        self.map = ListMap()
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
        self.assertEqual([key for key in self.map], ["a", "b", "c"])

    def test_len(self):
        self.assertEqual(len(self.map), 3)

    def test_keys(self):
        self.assertEqual(list(self.map.keys()), ["a", "b", "c"])
        
    def test_items(self):
        print(f'\nitems: {list(self.map.items())}')

    def test(self):
        self.test = HashMapBase()
        

if __name__ == "__main__":
    unittest.main(verbosity=2)
