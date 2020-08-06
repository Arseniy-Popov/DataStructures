import unittest

from deque import Deque


class TestDeque(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4]
        self.deque = Deque(self.data)

    def _compare_contents(self, deque=None, data=None):
        deque, data = deque or self.deque, data or self.data
        self.assertEqual([i for i in self.deque], data)

    def test_append_right(self):
        for i in range(self.deque._initialSize):
            self.deque.append(i)
            self.data.append(i)
            self._compare_contents()

    def test_pop_right(self):
        self.test_append_right()
        for _ in range(self.deque._initialSize):
            self.assertEqual(self.deque.pop(), self.data.pop())
            self._compare_contents()

    def test_pop_left(self):
        self.test_append_right()
        for _ in range(self.deque._initialSize):
            self.assertEqual(self.deque.popLeft(), self.data[0])
            del self.data[0]
            self._compare_contents()

    def test_append_left(self):
        for i in range(self.deque._initialSize):
            self.deque.appendLeft(i)
            self.data.insert(0, i)
            self._compare_contents()

    def test_shrink(self):
        self.data = []
        self.deque = Deque(self.data)
        for i in range(self.deque._initialSize + 1):
            self.deque.append(i)
            self.data.append(i)
        self.assertEqual(
            len(self.deque._array), self.deque._initialSize * self.deque._resizeFactor
        )
        for i in range(self.deque._initialSize + 1):
            self.deque.pop()
            self.data.pop()
            self._compare_contents()
        self.assertEqual(len(self.deque._array), self.deque._initialSize)


if __name__ == "__main__":
    unittest.main()
