def add_node(v):
    if v in graph:
        print(v, 'is already present in the graph')
    else:
        graph[v] = []


def add_edges(v1, v2):
    if v1 not in graph:
        print(v1, 'not present in the graph')
    elif v2 not in graph:
        print(v2, 'not present in the graph')
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)


# Using queue
def BFS(node, graph):
    visited = set()
    if node not in graph:
        print(node, 'is not present in the graph')
        return
    queue = []
    queue.append(node)
    while queue:
        current = queue.pop(0)
        if current not in visited:
            print(current, end=" ")
            visited.add(current)
            for i in graph[current]:
                queue.append(i)


if __name__ == '__main__':
    graph = {}
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
    BFS('E', graph)
