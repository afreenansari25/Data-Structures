"""
In Circular Linked list is same as singly list list but it in CLL last node contains the reference of first node
In Doubly Circular Linked List which is similar to doubly linked list, the last node contains the reference (next) of
first node and first node contains the reference (prev) of last node in addition to the reference (next) of second node.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print('List is empty!')
        else:
            n = self.head
            while True:
                print(n.data, end=' ')
                n = n.next
                if n == self.head:
                    break

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            n = self.head
            while n.next != self.head:
                n = n.next
            n.next = new_node
            new_node.next = self.head
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            n = self.head
            new_node.next = n
            while n.next != self.head:
                n = n.next
            n. next = new_node

    def add_given(self, x, data):
        new_node = Node(data)
        n = self.head
        while n.next != self.head:
            if n.data == x:
                break
            n = n.next
        if n.next == self.head and n.data != x:
            print(x, 'is not present in the list')
        else:
            new_node.next = n.next
            n.next = new_node

    def delete_begin(self):
        n = self.head
        if self.head is None:
            print('List is empty!')
            return
        if n.next == n:
            self.head = None
            return
        else:
            while n.next != self.head:
                n = n.next
            n.next = self.head.next
            self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print('List is empty!')
            return
        if self.head.next == self.head:
            self.head = None
            return
        else:
            n = self.head
            while n.next.next != self.head:
                n = n.next
            n.next = self.head

    def delete_given(self, x):
        n = self.head
        if self.head is None:               # case1: when list is empty
            print('List is empty!')
            return
        if self.head.data == x:             # case 2: To delete first node
            if self.head.next == n:             # when there is only one node
                self.head = None
            else:                               # where there are multiple nodes
                while n.next != self.head:
                    n = n.next
                n.next = self.head.next
                self.head = self.head.next
            return
        while n.next.next != self.head:     # case3: to delete any middle nodes
            if n.next.data == x:
                break
            n = n.next
        if n.next.next != self.head:
            n.next = n.next.next
        elif n.next.next == self.head and n.next.data == x:   # case4: To delete last node
            n.next = self.head
        else:
            print(x, 'is not present in the list')


if __name__ == '__main__':
    CLL = CircularLinkedList()
    CLL.add_begin(5)
    CLL.add_begin(3)
    CLL.add_begin(1)
    CLL.add_end(6)
    CLL.add_end(7)
    CLL.add_given(1, 2)
    CLL.add_given(7, 8)
    CLL.add_given(3, 4)
    CLL.delete_begin()
    CLL.delete_end()
    CLL.delete_given(2)
    CLL.delete_given(3)
    CLL.delete_given(4)
    CLL.delete_given(5)
    CLL.delete_given(6)
    CLL.delete_given(7)
    CLL.print_list()
