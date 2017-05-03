class unordered_graph(object):
 def __init__(self, V):
  self.V = V  # vertices
  self.E = 0  # edges
  self.bags = []
  for _ in range(self.V):
   self.bags.append([])

 def __str__(self):
  graph_str = ''
  for i in range(self.V):
   if len(self.bags[i]) > 0:
    graph_str = graph_str + 'Vertex: {}\nConnected vertices: {}\n'.format(i, self.bags[i])
  return str(graph_str)

 def __repr__(self):
  return self.__str__()

 def V(self):
  return self.V

 def E(self):
  return self.E

 def _validate_vertex(self, v):
  if v < 0 or v > self.V - 1:
   raise ValueError('Invalid vertex: {}. Vertex must be between 0 and {}'.format(v, self.V - 1))

 def adj(self, v):
  self._validate_vertex(v)
  return self.bags[v]

 def degree(self, v):
  self._validate_vertex(v)
  return len(self.bags[v])

 def add_edge(self, v, w):
  self._validate_vertex(v)
  self._validate_vertex(w)
  self.bags[v].append(w)
  self.bags[w].append(v)
  self.E = self.E + 1
