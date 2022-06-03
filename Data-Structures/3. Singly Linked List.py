"""
Singly linked list contains chain of Nodes, each node has data and a reference field.
In SLL head points to the first node and last node points to None.
SLL has three operations 1.Add 2.Remove and 3.Traversal(Printing each node)
"""


class Node:
    """This class will be used to create nodes"""
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        """This function will print each node in the list"""
        if self.head is None:
            print('List is empty!')
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" ")
                n = n.ref

    def add_begin(self, data):
        """This function will add the new node at the beginning of the list"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.ref = self.head
            self.head = new_node

    def add_end(self, data):
        """This function will add the new node at the end of the list"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_given(self, data, x):
        """This function will add the new node after a given node"""
        new_node = Node(data)
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print(x, 'is not present in the list!')
        else:
            new_node.ref = n.ref
            n.ref = new_node

    def delete_begin(self):
        """This function will delete the first node of the list"""
        if self.head is None:
            print('List is empty!')
        else:
            self.head = self.head.ref

    def delete_end(self):
        """This function will delete the last node of the list"""
        if self.head is None:
            print('List is empty!')
        elif self.head.ref is None:  # If there is only one node in the list
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:  # check for 2nd adjacent node, so that we can get second last node
                n = n.ref
            n.ref = None

    def delete_given(self, x):
        """This function will delete the given node of the list"""
        n = self.head
        if n.data == x:
            self.head = n.ref
            return
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print(x, 'is not present in the list!')
        else:
            n.ref = n.ref.ref

    def reverse_iterative(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.ref
            curr.ref = prev
            prev = curr
            curr = nxt
        self.head = prev

    def reverse_recursive(self, head):
        if head is None or head.ref is None:
            return head
        curr = self.reverse_recursive(head.ref)
        head.ref.ref = head
        head.ref = None
        return curr


if __name__ == '__main__':
    LL = LinkedList()
    LL.add_begin(5)
    LL.add_begin(2)
    LL.add_begin(1)
    LL.add_end(10)
    LL.add_end(15)
    LL.add_end(25)
    LL.add_given(12, 10)
    LL.add_given(50, 100)
    LL.delete_begin()
    LL.delete_end()
    LL.delete_given(15)
    LL.delete_given(1)
    LL.print_list()
    print()
    LL.reverse_iterative()
    LL.print_list()
    print()
    LL.head = LL.reverse_recursive(LL.head)
    LL.print_list()
