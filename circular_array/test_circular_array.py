import unittest

from circular_array import CircularArray


class TestCircularArray(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4]
        self.array = CircularArray(self.data)

    def _compare_contents(self, array=None, data=None):
        array, data = array or self.array, data or self.data
        self.assertEqual([i for i in self.array], data)

    def test_setitem(self):
        with self.subTest("positive"):
            self.array[1] = 5
            self._compare_contents(data=[1, 5, 3, 4])
        with self.subTest("negative"):
            self.array[-1] = 5
            self._compare_contents(data=[1, 5, 3, 5])

    def test_append_right(self):
        for i in range(self.array._initialSize):
            self.array.append(i)
            self.data.append(i)
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

    def test_insert(self):
        with self.subTest("front"):
            self.array.insert(1, 1)
            self._compare_contents(data=[1, 1, 2, 3, 4])
        with self.subTest("back"):
            self.array.insert(4, 1)
            self._compare_contents(data=[1, 1, 2, 3, 1, 4])
        with self.subTest("mid"):
            self.array.insert(3, 1)
            self._compare_contents(data=[1, 1, 2, 1, 3, 1, 4])

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


if __name__ == "__main__":
    unittest.main()
