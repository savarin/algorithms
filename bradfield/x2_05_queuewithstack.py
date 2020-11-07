'''
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.

Notes:
You must use only standard operations of a stack -- which means only push to
top, peek/pop from top, size, and is empty operations are valid.

Depending on your language, stack may not be supported natively. You may
simulate a stack by using a list or deque (double-ended queue), as long as you
use only standard operations of a stack.

You may assume that all operations are valid (for example, no pop or peek
operations will be called on an empty queue).
'''


class QueueWithStack():
    def __init__(self):
        self.stack = []
        self.reverse_stack = []

    def push(self, val):
        while len(self.reverse_stack) > 0:
            item = self.reverse_stack.pop()
            self.stack.append(item)            
        self.stack.append(val)

    def pop(self):
        while len(self.stack) > 0:
            item = self.stack.pop()
            self.reverse_stack.append(item)
        assert len(self.reverse_stack) > 0
        result = self.reverse_stack.pop()
        return result

    def peek(self):
        while len(self.stack) > 0:
            item = self.stack.pop()
            self.reverse_stack.append(item)
        if len(self.reverse_stack) > 0:
            return self.reverse_stack[-1]
        return None

    def empty(self):
        return len(self.stack) == 0 and len(self.reverse_stack) == 0
