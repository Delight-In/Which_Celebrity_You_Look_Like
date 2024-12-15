from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    # Add a vertex to the graph
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    # Add an edge between two vertices
    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # If it's an undirected graph

    # BFS traversal of the graph
    def bfs(self, start_vertex):
        visited = set()  # Set to keep track of visited vertices
        queue = deque([start_vertex])  # Queue to manage BFS order

        visited.add(start_vertex)
        bfs_result = []

        while queue:
            vertex = queue.popleft()
            bfs_result.append(vertex)

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return bfs_result

    # DFS traversal of the graph (recursive version)
    def dfs(self, start_vertex):
        visited = set()  # Set to keep track of visited vertices
        dfs_result = []

        def _dfs(vertex):
            visited.add(vertex)
            dfs_result.append(vertex)

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    _dfs(neighbor)

        _dfs(start_vertex)
        return dfs_result

    # Iterative DFS (using a stack)
    def dfs_iterative(self, start_vertex):
        visited = set()
        stack = [start_vertex]
        dfs_result = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                dfs_result.append(vertex)

                # Add all unvisited neighbors to the stack
                for neighbor in reversed(self.graph[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return dfs_result


# Example Usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)
    g.add_edge(4, 7)
    
    print("BFS starting from vertex 1:", g.bfs(1))  # Expected BFS traversal: [1, 2, 3, 4, 5, 6, 7]
    print("DFS starting from vertex 1 (recursive):", g.dfs(1))  # Expected DFS traversal: [1, 2, 4, 7, 5, 3, 6]
    print("DFS starting from vertex 1 (iterative):", g.dfs_iterative(1))  # Expected DFS traversal: [1, 3, 6, 2, 5, 4, 7]
