import unittest

from array_code import ArrayList
from lab4_1 import ArrayStack, push, pop, peek, is_empty


class TestArrayStack(unittest.TestCase):

    def test_push(self):
        s1 = ArrayStack(ArrayList(3, [None, None, None], 0))
        s2 = push(s1, 10)

        self.assertEqual(s1.stack.array, [None, None, None])
        self.assertEqual(s1.stack.next, 0)

        self.assertEqual(s2.stack.array, [10, None, None])
        self.assertEqual(s2.stack.next, 1)

    def test_peek(self):
        s1 = ArrayStack(ArrayList(3, [10, 20, None], 2))
        self.assertEqual(peek(s1), 20)

    def test_pop(self):
        s1 = ArrayStack(ArrayList(4, [10, 20, 30, None], 3))
        value, s2 = pop(s1)

        self.assertEqual(value, 30)
        self.assertEqual(s1.stack.array, [10, 20, 30, None])
        self.assertEqual(s1.stack.next, 3)

        self.assertEqual(s2.stack.array, [10, 20, None, None])
        self.assertEqual(s2.stack.next, 2)

    def test_is_empty(self):
        s1 = ArrayStack(ArrayList(3, [None, None, None], 0))
        s2 = ArrayStack(ArrayList(3, [5, None, None], 1))

        self.assertTrue(is_empty(s1))
        self.assertFalse(is_empty(s2))


if __name__ == "__main__":
    unittest.main()