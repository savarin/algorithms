'''
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.

Notes:
You must use only standard operations of a queue -- which means only push to
back, peek/pop from front, size, and is empty operations are valid.

Depending on your language, queue may not be supported natively. You may
simulate a queue by using a list or deque (double-ended queue), as long as you
use only standard operations of a queue.

You may assume that all operations are valid (for example, no pop or top
operations will be called on an empty stack).
'''


class StackWithQueue():
    def __init__(self):
        self.queue = []
        self.queue_helper = []

    def push(self, val):
        self.queue.append(val)

    def pop(self):
        while len(self.queue) > 1:
            item = self.queue.pop(0)
            self.queue_helper.append(item)
        result = self.queue.pop(0)
        self.queue, self.queue_helper = list(self.queue_helper), list(self.queue) 
        return result        

    def top(self):
        while len(self.queue) > 1:
            item = self.queue.pop(0)
            self.queue_helper.append(item)
        result = self.queue.pop(0)
        self.queue_helper.append(result)
        self.queue, self.queue_helper = list(self.queue_helper), list(self.queue) 
        return result

    def empty(self):
        return len(self.queue) == 0
