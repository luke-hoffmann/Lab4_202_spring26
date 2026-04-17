from dataclasses import dataclass


@dataclass
class ArrayList:
    size: int
    array: list[int | None]
    next: int = 0


def append(arr: ArrayList, n: int) -> ArrayList:
    """
    Returns a new ArrayList with n appended at the end.

    For now, this version raises IndexError if the list is full.
    Later in the lab, modify this function so that it automatically
    calls resize(arr) when needed.
    """
    arr2 = ArrayList(arr.size, arr.array.copy(), arr.next)

    if arr2.next == arr2.size:
        raise IndexError("ArrayList is full")

    arr2.array[arr2.next] = n
    arr2.next += 1
    return arr2


def delete(arr: ArrayList, index: int) -> ArrayList:
    """
    Returns a new ArrayList with the value at index removed.

    All later elements are shifted left so there are no gaps.

    Raises IndexError if the index is invalid.
    """
    if index < 0 or index >= arr.next:
        raise IndexError("Index out of bounds")

    arr2 = ArrayList(arr.size, arr.array.copy(), arr.next)

    for i in range(index, arr2.next - 1):
        arr2.array[i] = arr2.array[i + 1]

    arr2.next -= 1
    arr2.array[arr2.next] = None
    return arr2


def get(arr: ArrayList, index: int) -> int:
    """
    Returns the value at the given logical index.

    Raises IndexError if the index is invalid.
    """
    if index < 0 or index >= arr.next:
        raise IndexError("Index out of bounds")

    value = arr.array[index]
    if value is None:
        raise ValueError("No value stored at that index")

    return value


def resize(arr: ArrayList, factor: int = 2) -> ArrayList:
    """
    Returns a new ArrayList with a larger underlying array.

    Students:
    - Create a new list whose length is arr.size * factor
    - Copy over the existing elements
    - Return a new ArrayList with the new size, new array, and same next
    """
    new_size = arr.size * factor
    new_array = [None] * new_size

    for i in range(arr.next):
        new_array[i] = arr.array[i]

    return ArrayList(new_size, new_array, arr.next)


# -------------------------------------------------------------------
# Example usage
# -------------------------------------------------------------------
"""
arr1 = ArrayList(4, [None, None, None, None], 0)

arr2 = append(arr1, 10)
arr3 = append(arr2, 20)
arr4 = append(arr3, 30)

print("arr1:", arr1)
print("arr2:", arr2)
print("arr3:", arr3)
print("arr4:", arr4)

print("get(arr4, 1):", get(arr4, 1))

arr1 = ArrayList(5, [10, 20, 30, None, None], 3)
arr2 = delete(arr1, 1)

print(arr1)  # [10, 20, 30, None, None], next=3
print(arr2)  # [10, 30, None, None, None], next=2
"""