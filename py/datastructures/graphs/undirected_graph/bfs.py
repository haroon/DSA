"""Implementation of breadth first search on an undirected graph."""
from datetime import datetime
from random import seed, randint
from .undirected_graph import undirected_graph


class BFSPath(object):
    """BFS class."""
    def __init__(self, g, v):
        """Initialization routine."""
        self.graph = g
        self.vertex = v
        self.edge_from = None
        self.dist = None
        self.refresh()

    def refresh(self):
        """Refresh if the graph has been modified in some way."""
        self.edge_from = [None] * self.graph.V
        self.dist = [-1] * self.graph.V
        self._do_bfs()

    def _do_bfs(self):
        """Perform BFS on the graph and prepare path and shortest path lists."""
        k = 0
        self.dist[self.vertex] = k
        vertex_queue = [self.vertex]
        while len(vertex_queue) > 0:
            vertex = vertex_queue.pop(0)
            adjacent_vertices = self.graph.adj(vertex)
            for av in adjacent_vertices:
                if self.dist[av] == -1:
                    vertex_queue.append(av)
                    self.edge_from[av] = vertex
                    self.dist[av] = k
            k = k + 1

    def is_connected(self, s):
        """Check to see if a vertex is connected to the original vertex."""
        return self.dist[s] != -1

    def path_to(self, v):
        """Return the path to a vertex from the original vertex."""
        if not self.is_connected(v):
            return None
        path = [v]
        while v != self.vertex:
            v = self.edge_from[v]
            path.append(v)
        return path

    def shortest_dist(self, v):
        """Return the shortest distance from a vertex to the original vertex."""
        return self.dist[v]

MAX_VERTICES = 10


def test_ud_bfs_path():
    seed(datetime.now().timestamp())
    ug = undirected_graph(MAX_VERTICES)
    ug.add_edge(0, 1)
    ug.add_edge(1, 2)
    ug.add_edge(1, 3)
    ug.add_edge(2, 3)
    ug.add_edge(3, 4)
    ug.add_edge(4, 5)
    ug.add_edge(4, 6)
    ug.add_edge(5, 8)
    ug.add_edge(6, 9)

    print(ug)
    paths = BFSPath(ug, 3)
    print(paths.path_to(5))
    print(paths.shortest_dist(5))
