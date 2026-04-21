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
    if (s.write == None): 
        write = Node(v,None)
    else:
        write = new_head(v,s.write)
    return TwoStackQueue(s.read,write)
    
    


def dequeue(s: TwoStackQueue) -> tuple[int, TwoStackQueue]:
    """
    Returns a tuple (value, new_queue), where value is the
    front item removed from the queue.

    Raises IndexError if the queue is empty.
    """
    if is_empty(s): raise IndexError
    read = s.read
    write = s.write
    if s.read == None:
        write = None
        read = reverse(s.write)
    if read == None:
        raise IndexError
    value = read.value
    read = read.next
        
    return (value,TwoStackQueue(read,write))


def peek(s: TwoStackQueue) -> int:
    """
    Returns the front value without removing it.

    Raises IndexError if the queue is empty.
    """
    if is_empty(s): raise IndexError
    if is_empty(s): raise IndexError
    read = s.read
    write = s.write
    if s.read == None:
        write = None
        read = reverse(s.write)
    if read == None:
        raise IndexError
    value = read.value
    return value

def is_empty(s: TwoStackQueue) -> bool:
    """
    Returns True if the queue is empty, otherwise False.
    """
    return s.read is None and s.write is None