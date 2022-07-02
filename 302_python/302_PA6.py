# Dijkstra's Algorithm

# Each city is a node which points to next city
# Since Mpg is constant 40, all edges will have that value
# Dijkstra's algorithm preferred over other algorithms like bellmanford
# No negative weights, but less time, less overhead, more scalability
# For refresher from Algorithms: https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
