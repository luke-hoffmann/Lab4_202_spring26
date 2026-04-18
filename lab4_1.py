from dataclasses import dataclass
from array_code import ArrayList, append, delete, get


@dataclass
class ArrayStack:
    stack: ArrayList


def push(s: ArrayStack, n: int) -> ArrayStack:
    """
    Returns a new ArrayStack with n pushed onto the top.
    """
    return ArrayStack(append(s.stack,n))


def pop(s: ArrayStack) -> tuple[int, ArrayStack]:
    """
    Returns a tuple (value, new_stack), where value is the top item
    that was removed.

    Raises IndexError if the stack is empty.
    """
    if len(s.stack.array) ==0: raise IndexError
    value = s.stack.array[s.stack.next-1]
    if (value == None): raise IndexError
    stack = delete(s.stack,s.stack.next-1)
    return (value,ArrayStack(stack))

def peek(s: ArrayStack) -> int:
    """
    Returns the top value without removing it.

    Raises IndexError if the stack is empty.
    """
    if len(s.stack.array) ==0: raise IndexError
    value = s.stack.array[s.stack.next-1]
    if (value == None): raise IndexError
    return value


def is_empty(s: ArrayStack) -> bool:
    """
    Returns True if the stack is empty, otherwise False.
    """
    return s.stack.next == 0