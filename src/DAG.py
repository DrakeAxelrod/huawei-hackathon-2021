from collections import deque
class Graph(dict):

  def __init__(self,id=0, type=0, arrival=0, deadline=0):
    super().__init__()
    self.id = id
    self.type = type
    self.arrival = arrival
    self.deadline = deadline

  def add_node(self, node_name):
    """ add a node to the graph. """
    if node_name in self.keys():
      raise KeyError('node %s already exists' % node_name)
    self[node_name] = []

  def add_edge(self, node, dep_node):
    """ add an edge to the graph. """
    if node not in self or dep_node not in self:
      raise KeyError('one or more nodes do not exist in graph')
    else:
      self[node].append(dep_node)
      
  def delete_node(self, node):
    """ Delete a node from the graph. """
    del self[node]

  def delete_edge(self, node, dep_node):
    """ Delete an edge from the graph. """
    self[node].remove(dep_node)

  def node_predecessors(self, node):
    """ get all a nodes predecessors """
    return [key for key in self if node in self[key]]

  def node_deps(self, node):
      if node not in self:
          raise KeyError('node %s is not in graph' % node)
      return list(self[node])

  def all_deps(self):
    """ gets all the dependencies within the graph """
    all_deps = set()
    for deps in self.values():
      for dep in deps:
        all_deps.add(dep)
    return all_deps

  def all_leaves(self):
    """ get all nodes in the graph with no dependencies """
    return [key for key in self if not self[key]]

  def topological_sort(self):
    """ Returns a topological ordering of the DAG.
    Raises an error if this is not possible (graph is not valid).
    """
    in_degree = {}
    for u in self:
      in_degree[u] = 0

    for u in self:
      for v in self[u]:
        in_degree[v] += 1

    queue = deque()
    for u in in_degree:
      if in_degree[u] == 0:
        queue.appendleft(u)

    l = []
    while queue:
      u = queue.pop()
      l.append(u)
      for v in self[u]:
        in_degree[v] -= 1
        if in_degree[v] == 0:
          queue.appendleft(v)

    if len(l) == len(self):
      return l
    else:
      raise ValueError('graph is not acyclic')


  def cyclic(self):
    """Return True if the directed graph g has a cycle.
    g must be represented as a dictionary mapping vertices to
    iterables of neighbouring vertices. For example:
    >>> cyclic({1: (2,), 2: (3,), 3: (1,)})
    True
    >>> cyclic({1: (2,), 2: (3,), 3: (4,)})
    False
    """
    path = set()
    visited = set()

    def visit(vertex):
      if vertex in visited:
        return False
      visited.add(vertex)
      path.add(vertex)
      for neighbour in self.get(vertex, ()):
        if neighbour in path or visit(neighbour):
          return True
      path.remove(vertex)
      return False

    return any(visit(v) for v in self)
