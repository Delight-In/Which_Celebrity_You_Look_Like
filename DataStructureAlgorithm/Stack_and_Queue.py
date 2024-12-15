class Stack:
    def __init__(self):
        self.items = []

    # Push an item onto the stack
    def push(self, item):
        self.items.append(item)

    # Pop an item from the stack (remove and return the top element)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None  # Return None if the stack is empty

    # Peek at the top item of the stack without removing it
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    # Check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Get the size of the stack
    def size(self):
        return len(self.items)

    # String representation of the stack
    def __str__(self):
        return f"Stack({self.items})"

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)  # Stack([1, 2, 3])
print(stack.pop())  # 3
print(stack.peek())  # 2


class Queue:
    def __init__(self):
        self.items = []

    # Enqueue: Add an item to the back of the queue
    def enqueue(self, item):
        self.items.append(item)

    # Dequeue: Remove an item from the front of the queue and return it
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # Remove and return the first item
        return None  # Return None if the queue is empty

    # Peek at the front item of the queue without removing it
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    # Check if the queue is empty
    def is_empty(self):
        return len(self.items) == 0

    # Get the size of the queue
    def size(self):
        return len(self.items)

    # String representation of the queue
    def __str__(self):
        return f"Queue({self.items})"

# Example usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)  # Queue([1, 2, 3])
print(queue.dequeue())  # 1
print(queue.peek())  # 2
