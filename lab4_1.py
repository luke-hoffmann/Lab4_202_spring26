from dataclasses import dataclass
from array_code import ArrayList, append, delete, get


@dataclass
class ArrayStack:
    stack: ArrayList


def push(s: ArrayStack, n: int) -> ArrayStack:
    """
    Returns a new ArrayStack with n pushed onto the top.
    """
    pass


def pop(s: ArrayStack) -> tuple[int, ArrayStack]:
    """
    Returns a tuple (value, new_stack), where value is the top item
    that was removed.

    Raises IndexError if the stack is empty.
    """
    pass

def peek(s: ArrayStack) -> int:
    """
    Returns the top value without removing it.

    Raises IndexError if the stack is empty.
    """
    pass


def is_empty(s: ArrayStack) -> bool:
    """
    Returns True if the stack is empty, otherwise False.
    """
    return s.stack.next == 0