import unittest

from circular_array import CircularArray


class TestCircularArray(unittest.TestCase):
    def setUp(self):
        """
        [1, 2, 3, 4, 5, 6]
         0  1  2  3  4  5
        """
        self.data = [1, 2, 3, 4, 5, 6]
        self.array = CircularArray(self.data)

    def _compare_contents(self, array=None, data=None):
        array, data = array or self.array, data or self.data
        self.assertEqual([i for i in self.array], data)

    def _call_method(self, method, *args):
        getattr(self.array, method)(*args)
        getattr(self.data, method)(*args)

    def test_setitem(self):
        with self.subTest("positive"):
            self._call_method("__setitem__", 1, 5)
            self._compare_contents()
        with self.subTest("negative"):
            self._call_method("__setitem__", -1, 5)
            self._compare_contents()

    def test_insert(self):
        with self.subTest("front"):
            self._call_method("insert", 1, 1)
            self._compare_contents()
        with self.subTest("back"):
            self._call_method("insert", -2, 1)
            self._compare_contents()

    def test_delitem(self):
        with self.subTest("front"):
            self._call_method("__delitem__", 1)
            self._compare_contents()
        with self.subTest("back"):
            self._call_method("__delitem__", -2)
            self._compare_contents()

    def test_append_right(self):
        for i in range(self.array._initialSize+1):
            self._call_method("append", i)
            self._compare_contents()

    def test_pop_right(self):
        self.test_append_right()
        for _ in range(self.array._initialSize):
            self.assertEqual(self.array.pop(), self.data.pop())
            self._compare_contents()

    def test_pop_left(self):
        self.test_append_right()
        for _ in range(self.array._initialSize):
            self.assertEqual(self.array.popLeft(), self.data[0])
            del self.data[0]
            self._compare_contents()

    def test_append_left(self):
        for i in range(self.array._initialSize):
            self.array.appendLeft(i)
            self.data.insert(0, i)
            self._compare_contents()

    def test_shrink(self):
        self.data = []
        self.array = CircularArray(self.data)
        for i in range(self.array._initialSize + 1):
            self.array.append(i)
            self.data.append(i)
        self.assertEqual(
            len(self.array._array), self.array._initialSize * self.array._resizeFactor
        )
        for i in range(self.array._initialSize + 1):
            self.array.pop()
            self.data.pop()
            self._compare_contents()
        self.assertEqual(len(self.array._array), self.array._initialSize)

    def test_repr(self):
        self.assertEqual(str(self.array), f"<Deque {self.data}>")


if __name__ == "__main__":
    unittest.main()
