"""Implementation of undirected graph data structure"""


class undirected_graph(object):
    """Class representing an undirected graph."""
    def __init__(self, V=50):
        """Initialization method. Takes the number of vertices as a parameter."""
        self.V = V
        self.E = 0
        self.bags = []
        for _ in range(self.V):
            self.bags.append([])

    def __str__(self):
        """Readable string representation of the graph."""
        graph_str = ''
        for i in range(self.V):
            if len(self.bags[i]) > 0:
                graph_str = \
                 graph_str + 'Vertex: {}\nConnected vertices: {}\n'.format(i, self.bags[i])
        return str(graph_str)

    def __repr__(self):
        """String representation of the graph."""
        return self.__str__()

    def V(self):
        """Number of vertices in the graph."""
        return self.V

    def E(self):
        """Number of edges in the graph."""
        return self.E

    def adj(self, v):
        """Return all vertices connected to the specified vertex via an edge."""
        self._validate_vertex(v)
        return self.bags[v]

    def degree(self, v):
        """How many vertices are connected to a vertex."""
        self._validate_vertex(v)
        return len(self.bags[v])

    def add_edge(self, v, w):
        """Connect two vertices by an edge."""
        self._validate_vertex(v)
        self._validate_vertex(w)
        if not v in self.bags[w] and not w in self.bags[v]:
            self.bags[v].append(w)
            self.bags[w].append(v)
            self.E = self.E + 1

    def _validate_vertex(self, v):
        """Utility method to validate if a vertex is in the valid range."""
        if v < 0 or v > self.V - 1:
            raise ValueError(
                'Invalid vertex: {}. Vertex must be between 0 and {}'.format(v, self.V - 1))
