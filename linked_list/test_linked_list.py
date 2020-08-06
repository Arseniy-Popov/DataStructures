import unittest

from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.test_data = [10, "a", 20, 1, "d"]
        self.list = LinkedList(self.test_data)

    def _get_contents(self, linked_list):
        contents = []
        node = linked_list[0]
        while node is not None:
            contents.append(node.item)
            node = node.next()
        return contents

    def _compare_contents(self, test_contents, list=None):
        list = self.list if list is None else list
        list_contents = self._get_contents(list)
        self.assertEqual(list_contents, test_contents)

    def test_next_prev(self):
        list = LinkedList([1, 2])
        self.assertEqual(list[0].next().item, 2)
        self.assertEqual(list[-1].prev().item, 1)
        self.assertEqual(list[0].prev(), None)
        self.assertEqual(list[-1].next(), None)

    def test_insertAfter(self):
        self.list = LinkedList()
        with self.subTest("into empty"):
            self.list.append(10)
            self._compare_contents([10])
        with self.subTest("into non-empty"):
            self.list.append("a")
            self._compare_contents([10, "a"])
        with self.subTest("in between"):
            self.list.append(20, prev=self.list[0])
            self._compare_contents([10, 20, "a"])

    def test_insertBefore(self):
        self.list = LinkedList()
        with self.subTest("into empty"):
            self.list.prepend(10)
            self._compare_contents([10])
        with self.subTest("into non-empty"):
            self.list.prepend("a")
            self._compare_contents(["a", 10])
        with self.subTest("in between"):
            self.list.prepend(20, next=self.list[-1])
            self._compare_contents(["a", 20, 10])

    def test_delete(self):
        with self.subTest("first"):
            res = self.list.delete(self.list[0])
            del self.test_data[0]
            self._compare_contents(self.test_data)
            self.assertEqual(res.item, 10)
        with self.subTest("last"):
            res = self.list.delete(self.list[-1])
            del self.test_data[-1]
            self._compare_contents(self.test_data)
            self.assertEqual(res.item, "d")
        with self.subTest("in between"):
            item = self.list[0].next().item
            res = self.list.delete(self.list[0].next())
            del self.test_data[self.test_data.index(item)]
            self._compare_contents(self.test_data)
            self.assertEqual(res.item, 20)

    def test_bidirectional(self):
        self.test_delete()
        self.test_data.reverse()
        self.assertEqual([i.item for i in reversed(self.list)], self.test_data)

    def test_getitem(self):
        with self.subTest("front"):
            self.assertEqual(self.list[1].item, "a")
        with self.subTest("back"):
            self.assertEqual(self.list[3].item, 1)
        with self.subTest("negative"):
            self.assertEqual(self.list[-1].item, "d")

    def test_init(self):
        self._compare_contents(self.test_data)

    def test_iter(self):
        with self.subTest("forward"):
            self.assertEqual([x.item for x in self.list], self.test_data)
        with self.subTest("reverse"):
            self.test_data.reverse()
            self.assertEqual([x.item for x in reversed(self.list)], self.test_data)

    def test_len(self):
        with self.subTest("insertions"):
            self.assertEqual(len(self.list), len(self.test_data))
        with self.subTest("deletions"):
            self.list.delete(self.list[0])
            self.assertEqual(len(self.list), len(self.test_data) - 1)

    def test_index(self):
        self.assertEqual(self.list.index(1), 3)

    def test_contains(self):
        self.assertEqual(1 in self.list, True)
        self.assertEqual(15 in self.list, False)


if __name__ == "__main__":
    unittest.main()
