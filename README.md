# Lab 4: Stacks and Queues

This is a 3-day lab focusing on the **functional implementation** of stacks and queues. In a functional style, data structures are immutable; instead of modifying an existing structure, every operation returns a new version of that structure.

## Schedule

| Date | Topic | Data Structure |
| :--- | :--- | :--- |
| **Day 1** — April 20 | Array Stack | `ArrayList` wrapper |
| **Day 2** — April 22 | Array Queue | `ArrayList` wrapper |
| **Day 3** — April 24 | Linked List Stacks & Queues | Two-Stack Queue (Linked List) |

---

# Day 1 — April 20: Array Stack

In this part of the lab, you will complete the implementation of a stack built on top of an underlying array.

### Data Representation
The `ArrayStack` is a wrapper around an underlying `ArrayList` structure.

```python
@dataclass
class ArrayStack:
    stack: ArrayList
```

> [!IMPORTANT]
> **Functional Requirements:**
> * Do **not** mutate the original stack.
> * Always return a **new** `ArrayStack`.
> * The original stack must remain unchanged.

### Your Task
Complete the following functions in the provided template:
* `push`
* `pop`
* `peek`
* `is_empty`

### Pseudocode
* **`push(s, n)`**: Append `n` to the array; return a new stack.
* **`pop(s)`**: Get the top value; remove the top value; return both the value and the new stack.
* **`peek(s)`**: Return the top value without removing it.
* **`is_empty(s)`**: Check if the stack size is 0.

### Implementation Notes
* The **top** of the stack corresponds to the **last logical element** in the underlying array.
* `pop` must return a tuple: `(removed_value, new_stack)`.

---

# Day 2 — April 22: Array Queue

You will implement a queue using an underlying array, following the **First In, First Out (FIFO)** principle.

### Data Representation
```python
@dataclass
class ArrayQueue:
    queue: ArrayList
```

> [!IMPORTANT]
> This lab uses an **immutable/functional style**. Every operation must return a new queue state while leaving the original untouched. Use the helper functions from `array_code.py`.

### Queue Behavior
* **Enqueue:** Items are added at the **back** (end of the array).
* **Dequeue:** Items are removed from the **front** (index 0).
* **Peek:** Look at the **front** (index 0).

### Pseudocode
* **`enqueue(q, n)`**: Append `n` to the array; return a new queue.
* **`dequeue(q)`**: Get value at index 0; delete value at index 0; return both value and new queue.
* **`peek(q)`**: Return value at index 0.

### Deliverable
Complete the array-based queue functions in `lab4_2.py`.

---

# Day 3 — April 24: Linked List Stacks and TwoStackQueue

You will implement a queue using **two stacks**, where each stack is represented by an immutable linked list. This is a classic functional programming pattern to achieve efficient queue operations.

### Data Representation
```python
@dataclass(frozen=True)
class TwoStackQueue:
    read: Node | None = None
    write: Node | None = None
```
* **`read`**: A linked list storing items ready to be removed from the front.
* **`write`**: A linked list storing newly added items (in reverse order).

> [!IMPORTANT]
> **Immutability:** Both the linked lists and the `TwoStackQueue` wrapper are frozen. You must initialize and return new structures for every operation.

### Queue Logic
* **`enqueue(s, v)`**: 
    1. Add value `v` as the new head of the `write` stack.
    2. Return a new `TwoStackQueue`.
* **`dequeue(s)`**:
    1. If `read` is empty: Reverse the `write` stack and make it the new `read` stack.
    2. Remove the head of the `read` stack.
    3. Return the value and the new `TwoStackQueue`.
* **`peek(s)`**:
    1. If `read` is empty: Reverse `write` into `read`.
    2. Return the head value of the `read` stack.
* **`is_empty(s)`**:
    1. Returns `True` only if **both** `read` and `write` are empty.

### Implementation Notes
* Use `new_head` from `linked_list.py` to push onto the `write` stack.
* Use the `reverse` function when the `read` stack is empty.
* **Never** modify existing nodes.

### Deliverable
Complete the `TwoStackQueue` functions in `lab4_3.py`.