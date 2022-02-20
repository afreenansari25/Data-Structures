"""
Stack follows LIFO and it has two operations: push and pop
Stack can be implemented in three ways using: 1. List 2. deque class from 'collections' module 3. LifoQueue class from 'queue' module
"""

from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, data):
        self.container.append(data)

    def pop(self):
        if len(self.container) != 0:
            return self.container.pop()
        else:
            return 'Stack is empty'

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


if __name__ == '__main__':
    s = Stack()
    s.push(6)
    s.push(7)
    s.push(8)
    print('Length:', s.size())
    print('pop:', s.pop())
    print('peek:', s.peek())
    print(s.is_empty())
    print('pop:', s.pop())
    print('pop:', s.pop())
    print(s.is_empty())
    print('pop:', s.pop())
    print('pop:', s.pop())
    print('Length:', s.size())
