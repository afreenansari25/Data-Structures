"""
Graph contains 1. Node/vertex and 2.edges.
Types of graph :  Directed, undirected and weighted/un-wighted graph
Graph can be stored in memory using: 1. Adjacency Matrix 2. Adjacency list representations
Graph operations: 1. Insertion 2. Deletion 3. Traversal - using DFS and BFS
"""


# Using Adjacency Matrix representation for undirected-unweighted graph
# Insertion operation
def add_node(v):
    global node_count
    if v in nodes:
        print(v, 'is already present in the graph!')
    else:
        nodes.append(v)
        node_count += 1
        for i in graph:         # adding new column in matrix
            i.append(0)
        temp = []
        for i in range(node_count):     # adding row in matrix
            temp.append(0)
        graph.append(temp)


def add_edge(v1, v2):       # for weighted directed/undirected pass third parameter
    if v1 not in nodes:
        print(v1, 'is not present in the graph')
    elif v2 not in nodes:
        print(v2, 'is not present in the graph')
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 1   # graph[index1][index2] = weight, for weighted directed/undirected graph
        graph[index2][index1] = 1  # remove this row for directed graph


# Deletion operation
def delete_node(v):
    global node_count
    if v not in nodes:
        print(v, 'is not present in the graph')
    else:
        node_count -= 1
        index1 = nodes.index(v)
        nodes.pop(index1)
        graph.pop(index1)       # deleting row from matrix
        for i in graph:         # deleting column from matrix
            i.pop(index1)


def delete_edge(v1, v2):
    if v1 not in nodes:
        print(v1, 'is not present in the graph')
    elif v2 not in nodes:
        print(v2, 'is not present in the graph')
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 0
        graph[index2][index1] = 0   # remove this row for directed graph


def print_matrix():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j], end=" ")
        print()


if __name__ == '__main__':
    nodes = []
    graph = []
    node_count = 0
    add_node('A')
    add_node('B')
    add_node('C')
    add_node('D')
    print(nodes)
    add_edge('A', 'B')
    add_edge('A', 'C')
    add_edge('A', 'D')
    add_edge('B', 'C')
    print(graph)
    print_matrix()
    delete_node('C')
    print(nodes)
    delete_edge('A', 'C')
    print_matrix()


