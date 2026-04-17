from dataclasses import dataclass
from array_code import ArrayList, append, delete, get


@dataclass
class ArrayQueue:
    queue: ArrayList


def enqueue(q: ArrayQueue, n: int) -> ArrayQueue:
    """
    Returns a new ArrayQueue with n added to the back.
    """
    pass


def dequeue(q: ArrayQueue) -> tuple[int, ArrayQueue]:
    """
    Returns a tuple (value, new_queue), where value is the
    front item that was removed.

    Raises IndexError if the queue is empty.
    """
    pass


def peek(q: ArrayQueue) -> int:
    """
    Returns the front value without removing it.

    Raises IndexError if the queue is empty.
    """
    pass


def is_empty(q: ArrayQueue) -> bool:
    """
    Returns True if the queue is empty, otherwise False.
    """
    return q.queue.next == 0