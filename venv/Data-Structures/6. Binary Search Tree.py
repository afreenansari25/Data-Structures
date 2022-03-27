"""
There are two types of tree 1. General tree 2. Binary tree.
In general tree, a node can have any number of children.
In Binary tree, a node can have at most 2 children i.e 0,1 and 2.
Binary Search Tree(BST) is a special type of binary tree where left child should be less than root node and right child
should be greater than root node.
BST operations: insert, search, traversal, delete, min & max keys etc.
"""


class BST:
    def __init__(self, key):
        self.key = key
        self.l_child = None
        self.r_child = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:    # to avoid duplicate node insertion, duplicate node will be ignored
            return
        if data < self.key:     # traverse left sub-tree if data is less than root node
            if self.l_child:
                self.l_child.insert(data)
            else:
                self.l_child = BST(data)
        else:                   # traverse right subtree if data is greater than root node
            if self.r_child:
                self.r_child.insert(data)
            else:
                self.r_child = BST(data)

    def search(self, data):
        if self.key == data:
            print(data, 'found in tree.')
        else:
            if data < self.key:
                if self.l_child:
                    self.l_child.search(data)
                else:
                    print('Node is not found!')
            else:
                if self.r_child:
                    self.r_child.search(data)
                else:
                    print('Node is not found!')

    # Traversal operation
    # 1. Preorder: root->left node-> right node
    def pre_order(self):
        print(self.key, end=" ")
        if self.l_child:
            self.l_child.pre_order()
        if self.r_child:
            self.r_child.pre_order()

    # 2. Inorder: left node-> root-> right node
    def in_order(self):
        if self.l_child:
            self.l_child.in_order()
        print(self.key, end=" ")
        if self.r_child:
            self.r_child.in_order()

    # 3. Postorder: left node -> right node -> root
    def post_order(self):
        if self.l_child:
            self.l_child.post_order()
        if self.r_child:
            self.r_child.post_order()
        print(self.key, end=" ")

    # Deletion operation
    def delete(self, data, curr):
        if self.key is None:
            print('Tree is empty!')
            return
        if data < self.key:
            if self.l_child:
                self.l_child = self.l_child.delete(data, curr)
            else:
                print('Node is not present in the tree')
        elif data > self.key:
            if self.r_child:
                self.r_child = self.r_child.delete(data, curr)
            else:
                print('Node is not present in the tree')
        else:                           # we are on node that needs to be deleted
            if self.l_child is None:    # Case1: if the node to be deleted has 1 right child or zero child
                temp = self.r_child
                if data == curr:        # to check if node to be deleted is the root node
                    self.key = temp.key
                    self.l_child = temp.l_child
                    self.r_child = temp.r_child
                    # temp = None
                    return
                # self = None
                return temp
            if self.r_child is None:    # Case 2: if the node to be deleted has 1 left child or zero child
                temp = self.l_child
                if data == curr:
                    self.key = temp.key
                    self.l_child = temp.l_child
                    self.r_child = temp.r_child
                    # temp = None
                    return
                # self = None
                return temp

            """ Case3: if node to be deleted has 2 children: either replace the node with greatest node present in left 
            sub-tree or smallest node present in right subtree. We are following second approach. """
            node = self.r_child
            while node.l_child:
                node = node.l_child
            self.key = node.key
            self.r_child = self.r_child.delete(node.key, curr)
        return self

    # methods to find out smallest and largest key in the tree
    def find_min(self):
        while self.l_child is not None:
            self = self.l_child
        print('Min node:', self.key)

    def find_max(self):
        while self.r_child is not None:
            self = self.r_child
        print('Max node:', self.key)


def count(node):
    if node is None:
        return 0
    return 1+count(node.l_child)+count(node.r_child)


if __name__ == '__main__':
    root = BST(5)
    list1 = [8, 7, 6, 3]
    for i in list1:
        root.insert(i)
    print('Preorder:', end=" ")
    root.pre_order()
    print()
    print('Inorder:', end=" ")
    root.in_order()
    print()
    print('Postorder', end=" ")
    root.post_order()
    print()
    if count(root) > 1:
        root.delete(7, root.key)
    else:
        print('Cannot perform deletion operation')
    print('After deletion:', end=" ")
    root.in_order()
    print()
    print('No. of nodes:', count(root))
    root.find_min()
    root.find_max()
