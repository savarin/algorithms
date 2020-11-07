
'''
Design a stack that supports push, pop, top, and retrieving the minimum
element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''


class MinStack():
    def __init__(self):
        self.stack = []

    def push(self, val):
        if len(self.stack) == 0:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))

    def pop(self):
        item = self.stack.pop()
        return item[0]

    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1][0]
        return None

    def get_min(self):
        return self.stack[-1][1]
