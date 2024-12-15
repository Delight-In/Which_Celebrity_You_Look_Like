# How to find Shortest Paths from Source to all Vertices using Dijkstra’s Algorithm

import heapq

class Graph:
    def __init__(self):
        # Dictionary to hold adjacency list of the graph: {vertex: [(neighbor, weight), ...]}
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        self.graph[vertex1].append((vertex2, weight))
        self.graph[vertex2].append((vertex1, weight))  # For undirected graph

    def dijkstra(self, start_vertex):
        # Initialize distances and priority queue
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]  # (distance, vertex)

        while priority_queue:
            # Get the vertex with the smallest distance
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # If the current distance is greater than the recorded distance, skip it
            if current_distance > distances[current_vertex]:
                continue

            # Explore the neighbors
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                # If a shorter path is found, update the distance and add the neighbor to the queue
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

# Example Usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2, 4)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 3, 2)
    g.add_edge(2, 4, 5)
    g.add_edge(3, 4, 1)

    # Find shortest paths from vertex 1
    shortest_paths = g.dijkstra(1)
    print("Shortest paths from vertex 1:", shortest_paths)
