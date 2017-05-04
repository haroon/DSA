"""Implementation of breadth first search on an undirected graph."""
from datetime import datetime
from random import seed, randint
from .undirected_graph import undirected_graph


class DFSPath(object):
    """DFS class."""
    def __init__(self, g, v):
        """Initialization routine."""
        self.graph = g
        self.vertex = v
        self.edge_from = None
        self.visited = None
        self.refresh()

    def refresh(self):
        """Refresh if the graph has been modified in some way."""
        self.edge_from = [None] * self.graph.V
        self.visited = [False] * self.graph.V
        self._do_dfs(self.vertex)

    def _do_dfs(self, vertex):
        """Perform DFS on the graph and prepare path and shortest path lists."""
        self.visited[vertex] = True
        adjacent_vertices = self.graph.adj(vertex)
        for v in adjacent_vertices:
            if not self.visited[v]:
                self._do_dfs(v)
                self.edge_from[v] = vertex

    def is_connected(self, s):
        """Check to see if a vertex is connected to the original vertex."""
        return self.visited[s]

    def path_to(self, v):
        """Return the path to a vertex from the original vertex."""
        if not self.is_connected(v):
            return None
        path = [v]
        while v != self.vertex:
            v = self.edge_from[v]
            path.append(v)
        return path

MAX_VERTICES = 20


def test_ud_dfs_path():
    seed(datetime.now().timestamp())
    ug = undirected_graph(MAX_VERTICES)

    test_vertices = []

    for i in range(MAX_VERTICES):
        v1 = randint(0, MAX_VERTICES - 1)
        v2 = randint(0, MAX_VERTICES - 1)
        test_vertices.append((v1, v2))
        ug.add_edge(v1, v2)

    print(test_vertices)

    v = randint(0, MAX_VERTICES - 1)
    print(v)
    paths = DFSPath(ug, v)
    v = randint(0, MAX_VERTICES - 1)
    print(v)
    path = paths.path_to(v)
    print(path)
