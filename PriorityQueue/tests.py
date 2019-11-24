import unittest
from PriorityQueue import PriorityQueue


class test_priotityQueue(unittest.TestCase):
    def build_queue(self):
        self.queue = PriorityQueue(sorted=True)

    def populate_queue(self):
        self.queue.add("s", 5)
        self.queue.add("r", 2)
        self.queue.add("d", 3)
        self.queue.add("h", 15)
        self.queue.add("q", 1)
        self.queue.add("w", 20)
        self.queue.add("e", 7)

    def setUp(self):
        self.build_queue()
        self.populate_queue()

    def test_min(self):
        self.assertEqual(self.queue.min(), ("q", 1))

    def test_removeMin(self):
        result = self.queue.removeMin()
        self.assertEqual(result, ("q", 1))
        self.assertEqual(len(self.queue), 6)

    def test_removeMin_multiple(self):
        result = []
        while len(self.queue) > 0:
            result.append(self.queue.removeMin()[1])
        self.assertEqual(result, [1, 2, 3, 5, 7, 15, 20])
        self.assertRaises(ValueError, self.queue.removeMin)


class test_sorted(test_priotityQueue):
    def priorities(self, queue):
        result = []
        for position in queue.data:
            result.append(position.node.item.priority)
        return result

    def build_queue(self):
        self.queue = PriorityQueue(sorted=True)

    def test_order(self):
        self.assertEqual(self.priorities(self.queue), [1, 2, 3, 5, 7, 15, 20])


if __name__ == "__main__":
    unittest.main()
