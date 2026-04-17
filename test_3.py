import unittest

from lab4_3 import TwoStackQueue, enqueue, dequeue, peek, is_empty
from linked_list import Node


class TestTwoStackQueue(unittest.TestCase):

    def test_enqueue(self):
        q1 = TwoStackQueue()
        q2 = enqueue(q1, 10)

        self.assertIsNone(q1.read)
        self.assertIsNone(q1.write)

        self.assertIsNone(q2.read)
        self.assertEqual(q2.write, Node(10, None))

    def test_dequeue(self):
        q1 = TwoStackQueue(
            read=Node(10, Node(20, None)),
            write=None
        )

        value, q2 = dequeue(q1)

        self.assertEqual(value, 10)
        self.assertEqual(q1.read, Node(10, Node(20, None)))
        self.assertIsNone(q1.write)

        self.assertEqual(q2.read, Node(20, None))
        self.assertIsNone(q2.write)

    def test_peek(self):
        q1 = TwoStackQueue(
            read=Node(10, Node(20, None)),
            write=None
        )

        self.assertEqual(peek(q1), 10)

    def test_is_empty(self):
        q1 = TwoStackQueue()
        q2 = TwoStackQueue(read=Node(5, None), write=None)

        self.assertTrue(is_empty(q1))
        self.assertFalse(is_empty(q2))


if __name__ == "__main__":
    unittest.main()