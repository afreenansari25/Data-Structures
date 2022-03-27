"""
In DLL every node had a data filed and two pointers 1.next:points to the next node 2.prev: points to the previous node
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        """print_list method will print all the nodes present in DLL"""
        if self.head is None:
            print('List is empty!')
        else:
            n = self.head
            while n is not None:
                print(n.data, end=' ')
                n = n.next

    def add_begin(self, data):
        """add_begin method will add the new node at the beginning of DLL"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            new_node.next.prev = new_node
            self.head = new_node

    def add_end(self, data):
        """add_end method will add the new node at the end of the DLL"""
        new_node = Node(data)
        if self.head is None:   # if list is empty then point head to new node
            self.head = new_node
        else:                   # else traverse through the list and add the node at the end
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
            new_node.prev = n

    def add_given(self, x, data):
        """add_given method will at the new node after a given node"""
        new_node = Node(data)
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.next
        if n is not None:
            new_node.prev = n
            new_node.next = n.next
            n.next.prev = new_node
            n.next = new_node
        else:
            print(x, 'is not present in the list!')

    def delete_begin(self):
        """delete_begin will delete the first node of the DLL"""
        if self.head is None:
            print('List is empty!')
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_end(self):
        """delete_end will delete the last node of DLL"""
        n = self.head
        if self.head is None:
            print('List is empty')
        elif self.head.next is None:
            self.head = None
        else:
            while n.next.next is not None:
                n = n.next
            n.next = None

    def delete_given(self, x):
        """delete_given will delete any given node from DLL"""
        if self.head is None:
            print('List is empty!')
            return
        if self.head.next is None:      # case 1: If list has only one node:
            if self.head.data == x:
                self.head = None
            else:
                print(x, 'is not present in the list!')
            return
        if self.head.data == x:         # case 2: to delete 1st node
            self.head = self.head.next
            self.head.prev = None
            return
        n = self.head
        while n.next is not None:
            if n.data == x:
                break
            n = n.next
        if n.next is not None:          # case 3: to delete any middle node
            n.next.prev = n.prev
            n.prev.next = n.next
        else:
            if n.data == x:             # case 4: to delete last node
                n.prev.next = None
            else:
                print(x, 'is not present in the list')


if __name__ == '__main__':
    LL = DoublyLinkedList()
    LL.add_begin(3)
    LL.add_begin(2)
    LL.add_end(4)
    LL.add_end(5)
    LL.add_begin(1)
    LL.add_given(2, 0)
    LL.print_list()
    print()
    LL.delete_begin()
    LL.delete_end()
    LL.delete_given(2)
    LL.delete_given(0)
    LL.delete_given(3)
    LL.delete_given(4)
    LL.print_list()
