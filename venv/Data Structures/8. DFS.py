# Using Adjacency List graph representation and unweighted-undirected graph
def add_node(v):
    if v in graph:
        print(v, 'is already present in the graph')
    else:
        graph[v] = []


def add_edges(v1, v2):
    if v1 not in graph:
        print(v1, 'is not present in the graph')
    elif v2 not in graph:
        print(v2, 'is not present in the graph')
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)


def delete_node(v):
    if v not in graph:
        print(v, 'is not present in the graph')
    else:
        graph.pop(v)
        for i in graph:
            if v in graph[i]:
                graph[i].remove(v)


def delete_edge(v1, v2):
    if v1 not in graph:
        print(v1, 'is not present in the graph')
    elif v2 not in graph:
        print(v2, 'is not present in the graph')
    else:
        graph[v1].remove(v2)
        graph[v2].remove(v1)


# DFS using recursion
def DFS(node, visited, graph):
    if node not in graph:
        print(node, 'is not present in the graph')
        return
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for i in graph[node]:
            DFS(i, visited, graph)


# DFS using iterative approach (using stack)
def DFS_iterative(node, graph):
    visited = set()
    if node not in graph:
        print(node, 'is not present in the graph')
        return
    stack = []
    stack.append(node)          # push first node in th stack
    while stack:
        current = stack.pop()   # pop last node from the stack
        if current not in visited:
            print(current, end=" ")
            visited.add(current)
            for i in graph[current]:
                stack.append(i)     # push all the connected node in the stack


if __name__ == '__main__':
    graph = {}
    visited = set()
    add_node('A')
    add_node('B')
    add_node('C')
    add_node('D')
    add_node('E')
    add_edges('A', 'B')
    add_edges('A', 'C')
    add_edges('B', 'C')
    add_edges('B', 'D')
    add_edges('C', 'E')
    add_edges('D', 'E')
    # delete_node('D')
    # delete_edge('A','C')
    print(graph)
    DFS('A', visited, graph)
    print()
    DFS_iterative('A', graph)
