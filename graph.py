from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_util(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")

        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def depth_first_search(self, start_vertex):
        visited = [False] * len(self.graph)
        self.dfs_util(start_vertex, visited)
        print()

    def breadth_first_search(self, start_vertex):
        visited = [False] * len(self.graph)
        queue = deque()
        queue.append(start_vertex)
        visited[start_vertex] = True

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in self.graph[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        print()


g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Depth-First Traversal (DFS):")
g.depth_first_search(2)
print("Breadth-First Traversal (BFS):")
g.breadth_first_search(2)
