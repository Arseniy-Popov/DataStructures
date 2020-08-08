import random
import unittest

from heap import Heap


class TestHeap(unittest.TestCase):
    def setUp(self):
        self.heap = Heap()
        self.items = random.choices(range(100), k=30)

    def test_push_peek(self):
        items = []
        for i in self.items:
            self.heap.push(i)
            items.append(i)
            self.assertEqual(min(items), self.heap.peek())

    def test_peek(self):
        with self.assertRaises(IndexError):
            self.heap.peek()

    def test_pop(self):
        items = self.items
        for i in self.items:
            self.heap.push(i)
        for i in self.items:
            self.assertEqual(self.heap.pop(), min(items))
            items.remove(min(items))

    def test_len(self):
        n = 5
        with self.subTest("push"):
            for i in range(n):
                self.heap.push(1)
                self.assertEqual(len(self.heap), i+1)
        with self.subTest("peek"):
            self.heap.peek()
            self.assertEqual(len(self.heap), n)
        with self.subTest("pop"):
            for i in range(n):
                self.heap.pop()
                self.assertEqual(len(self.heap), n-i-1)
    
    def test_contains(self):
        items = []
        for i in self.items:
            self.heap.push(i)
            items.append(i) 
            for j in items:
                self.assertEqual(j in self.heap, True)
    
    def test_repr(self):
        items = []
        for i in self.items:
            self.heap.push(i)
            items.append(i)
        length, min_ = len(items), min(items)
        self.assertEqual(str(self.heap), f"<Heap of lenght {length}, min: {min_}>")
        
    def test_key(self):
        heap = Heap(lambda x: -x)
        items = []
        for i in self.items:
            heap.push(i)
            items.append(i)
            self.assertEqual(heap.peek(), max(items))
            
            
if __name__ == "__main__":
    unittest.main()
