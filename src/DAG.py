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

  def topological_sort(self, start):
    path = []
    stack = [start]
    label = len(self)
    result = {}
    while stack != []:
        #this for loop could be done in other ways also
        for element in stack:
            if element not in result:
                result[element] = label
                label = label - 1
        v = stack.pop()
        if v not in path:
          path.append(v)
        for w in reversed(self[v]):
            if w not in path and not w in stack:
                stack.append(w)
    result = {v: k for k, v in result.items()}
    return path, result


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
