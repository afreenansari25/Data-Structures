"""
Queue follows FIFO and has two ends 1. head/front - from where elements are removed 2. tail/rear - from where the elements are entered
Process or removing the element is called dequeue and process of entering the element is called enqueue
Queue can be implemented in three ways using: 1. List 2. deque class from 'collections' module 3. Queue class from 'queue' module
Queue operations: enqueue, dequeue, is_empty and is_full
Note: We also have priority queue where elements are removed from the queue based on priority. 
"""

from collections import deque


class Queue:
    def __init__(self, size):
        self.container = deque()
        self.size = size

    def enqueue(self, data):
        if len(self.container) != self.size:
            self.container.append(data)
        else:
            self.is_full()

    def dequeue(self):
        return self.container.popleft()

    def is_empty(self):
        return len(self.container) == 0

    def is_full(self):
        if len(self.container) == self.size:
            print('Queue is full')
        else:
            print('Queue is not full')

    def queue_size(self):
        print(len(self.container))


if __name__ == '__main__':
    q = Queue(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.queue_size()
    q.enqueue(4)
    print(q.dequeue())
    q.is_full()
    print(q.is_empty())










