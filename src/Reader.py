import json
from src.Graph import Graph
from src.Task import Task

def read_file(filename):
  with open(filename) as f:
    file = json.load(f)
    f.close()
  return file
  
def read_data(filename) -> list[Graph]:
  # local list to populate with graphs
  # I dont know if list is actually the best data structure here
  graphList: list[Graph] = []
  data = read_file(filename)
  for dagID, dagData in data.items():
    # dependent list for populating the edges of the graph
    tmpDependentDict = {}
    # step 1) this is enough data to make the initial empty graph
    dagType = dagData["Type"]
    arrival = dagData["ArrivalTime"]
    deadline = dagData["Deadline"]
    graph = Graph(dagID, dagType, arrival, deadline)
    # step 2) after you initialize your basic (no node no edge graph) we populate nodes
    # filter dagData for the tasks (nodes)
    taskKeys = filter(lambda key: type(dagData[key]) is dict, dagData)
    for taskID in taskKeys:
      taskData: dict = dagData[taskID]
      # at this point we can start making tasks
      graph.taskList[taskID] = Task(taskID, taskData["EET"], taskData["Type"])
      graph.add_node(taskID)
      # tmp dependency list
      for dep, transferTime in taskData["next"].items():
        if not dep in tmpDependentDict.keys():
          tmpDependentDict[dep] = []
          tmpDependentDict[dep].append((taskID, transferTime))
        else:
          tmpDependentDict[dep].append((taskID, transferTime))
    # add edges lil wonky but results seem correct
    for dependentsID, dependencies in tmpDependentDict.items():
      for dependency in dependencies:
        dep = dependency[0]
        weight = dependency[1]
        graph.add_edge(dependentsID, dep, weight)
    graphList.append(graph)
  return graphList

data = read_data("./src/sample.json")
