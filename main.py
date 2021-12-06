import sys
import statistics
from src.Processor import Processor
from src.Task import Task
import src.Visualization
from time import process_time_ns
from src.playground import playground
from src.Graph import Graph
from src.IO import read_data, write_data, listOfProcessors


def calculate_time(begin, end):
  elapsed = end - begin
  time_milliseconds = int((elapsed) * 0.001)
  time_microseconds = (elapsed) 
  print(f"time: { time_milliseconds }ms - milliseconds | { time_microseconds }μs - microseconds")
  return (time_microseconds, time_microseconds)

def calculate_standard_deviation(ListOfProcessors, makespan):
  listOfProcExeTime: list[Processor] = [proc.exeTime/makespan for proc in ListOfProcessors]
  return statistics.pstdev(listOfProcExeTime)
  
def schedule_task(task: Task):
  global listOfProcessors
  print(task)

def schedule_graph(dag: Graph):
  topologicalOrder = dag.topological_sort()
  for taskID in topologicalOrder:
    schedule_task(dag.taskList[taskID])

def scheduler(listOfDags: list[Graph]):
  for dag in listOfDags:
    schedule_graph(dag)

def run():
  listOfDags: list[Graph] = read_data("./src/sample.json") # returns a list of graphs
  begin = process_time_ns()
  scheduler(listOfDags)
  end = process_time_ns()
  time_results = calculate_time(begin, end) # returns a tuple of time results as (microseconds, nanoseconds)
  write_data("./src/output/sample.csv", [], 0, 0, 0, time_results[0])
  
if __name__ == "__main__":
  #playground()
  run()
