from dataclasses import dataclass
from linked_list import Node, new_head, reverse


@dataclass(frozen=True)
class TwoStackQueue:
    """
    A queue implemented using two immutable linked-list stacks.

    - read stores elements ready to be dequeued
    - write stores newly enqueued elements
    """
    read: Node | None = None
    write: Node | None = None


def enqueue(s: TwoStackQueue, v: int) -> TwoStackQueue:
    """
    Returns a new TwoStackQueue with v added to the back.
    """
    pass


def dequeue(s: TwoStackQueue) -> tuple[int, TwoStackQueue]:
    """
    Returns a tuple (value, new_queue), where value is the
    front item removed from the queue.

    Raises IndexError if the queue is empty.
    """
    pass


def peek(s: TwoStackQueue) -> int:
    """
    Returns the front value without removing it.

    Raises IndexError if the queue is empty.
    """
    pass


def is_empty(s: TwoStackQueue) -> bool:
    """
    Returns True if the queue is empty, otherwise False.
    """
    return s.read is None and s.write is None