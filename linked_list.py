from dataclasses import dataclass


@dataclass(frozen=True)
class Node:
    value: int
    next: "Node | None" = None


def append(head: Node | None, n: int) -> Node:
    """
    Returns a new linked list with n appended at the end.
    """
    if head is None:
        return Node(n)

    return Node(head.value, append(head.next, n))


def delete(head: Node | None, index: int) -> Node | None:
    """
    Returns a new linked list with the node at index removed.

    Raises IndexError if the index is invalid.
    """
    if index < 0:
        raise IndexError("Index out of bounds")

    if head is None:
        raise IndexError("Index out of bounds")

    if index == 0:
        return head.next

    return Node(head.value, delete(head.next, index - 1))


def new_head(value: int, head: Node | None) -> Node:
    """
    Returns a new head node whose next points to the old list.
    """
    return Node(value, head)


def reverse(head: Node | None, acc: Node | None = None) -> Node | None:
    """
    Returns a new reversed linked list.
    """
    if head is None:
        return acc

    return reverse(head.next, new_head(head.value, acc))