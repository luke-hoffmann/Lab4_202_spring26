from dataclasses import dataclass
from array_code import ArrayList, append, delete, get


@dataclass
class ArrayQueue:
    queue: ArrayList


def enqueue(q: ArrayQueue, n: int) -> ArrayQueue:
    """
    Returns a new ArrayQueue with n added to the back.
    """
    return ArrayQueue(append(q.queue,n))


def dequeue(q: ArrayQueue) -> tuple[int, ArrayQueue]:
    """
    Returns a tuple (value, new_queue), where value is the
    front item that was removed.

    Raises IndexError if the queue is empty.
    """
    if len(q.queue.array) == 0: raise IndexError
    value = q.queue.array[0]
    if value == None: raise IndexError
    return (value, ArrayQueue(delete(q.queue,0)))

def peek(q: ArrayQueue) -> int:
    """
    Returns the front value without removing it.

    Raises IndexError if the queue is empty.
    """
    value = q.queue.array[0]
    if value == None: raise IndexError
    return value


def is_empty(q: ArrayQueue) -> bool:
    """
    Returns True if the queue is empty, otherwise False.
    """
    return q.queue.next == 0