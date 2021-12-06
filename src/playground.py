from .Graph import Graph
import random

def playground():
  graph = Graph(0,0,0,0)
  n = 5

  # init nodes
  for i in range(n):
    graph.add_node(i)

  # init random dependencies
  for i in graph:
    for i in range(random.randint(0, random.choice(range(n)))):
      # populate (and make sure it isnt cyclic)
      new_dep = random.choice(list(graph.keys()))
      graph.add_edge(i, new_dep, 0)
      while graph.cyclic():
        graph.delete_edge(i, new_dep)
        new_dep = random.choice(list(graph.keys()))
        graph.add_edge(i, new_dep)

  print(graph)
  # print(graph.cyclic())
  print(graph.topological_sort())
      
