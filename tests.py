import unittest
from Heap import Heap
from PriorityQueue.tests import test_priotityQueue


class test_heap(test_priotityQueue):
    def build_queue(self):
        self.queue = Heap()

    def priorities(self, target):
        result = []
        for i in target.data:
            result.append(i.priority)
        return result

    def test_parent_index(self):
        self.assertEqual(self.queue._parent(5), 2)
        self.assertEqual(self.queue._parent(6), 2)
        self.assertEqual(self.queue._parent(2), 0)

    def test_child_index(self):
        self.assertEqual(self.queue._left(1), 3)
        self.assertEqual(self.queue._right(1), 4)
        self.assertEqual(self.queue._left(6), None)

    def test_priorities(self):
        print(self.priorities(self.queue))

    def test_removeMin_multiple(self):
        result = []
        while len(self.queue) > 0:
            result.append(self.queue.removeMin()[1])
            print(self.priorities(self.queue))
        self.assertEqual(result, [1, 2, 3, 5, 7, 15, 20])

    def test_buildup(self):
        self.queue2 = Heap()
        tuples = [
            ("s", 5),
            ("r", 2),
            ("d", 3),
            ("h", 15),
            ("q", 1),
            ("w", 20),
            ("e", 7),
        ]
        for i in tuples:
            self.queue2.add(i[0], i[1])
            print(self.priorities(self.queue2))


if __name__ == "__main__":
    tests = []
    # repeat line for each class
    tests.append(unittest.TestLoader().loadTestsFromTestCase(test_heap))
    suite = unittest.TestSuite(tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
