import unittest

from array_code import ArrayList
from lab4_2 import ArrayQueue, enqueue, dequeue, peek, is_empty


class TestArrayQueue(unittest.TestCase):

    def test_enqueue(self):
        q1 = ArrayQueue(ArrayList(3, [None, None, None], 0))
        q2 = enqueue(q1, 10)

        self.assertEqual(q1.queue.array, [None, None, None])
        self.assertEqual(q1.queue.next, 0)

        self.assertEqual(q2.queue.array, [10, None, None])
        self.assertEqual(q2.queue.next, 1)

    def test_peek(self):
        q1 = ArrayQueue(ArrayList(3, [10, 20, None], 2))
        self.assertEqual(peek(q1), 10)

    def test_dequeue(self):
        q1 = ArrayQueue(ArrayList(4, [10, 20, 30, None], 3))
        value, q2 = dequeue(q1)

        self.assertEqual(value, 10)
        self.assertEqual(q1.queue.array, [10, 20, 30, None])
        self.assertEqual(q1.queue.next, 3)

        self.assertEqual(q2.queue.array, [20, 30, None, None])
        self.assertEqual(q2.queue.next, 2)

    def test_is_empty(self):
        q1 = ArrayQueue(ArrayList(3, [None, None, None], 0))
        q2 = ArrayQueue(ArrayList(3, [5, None, None], 1))

        self.assertTrue(is_empty(q1))
        self.assertFalse(is_empty(q2))


if __name__ == "__main__":
    unittest.main()