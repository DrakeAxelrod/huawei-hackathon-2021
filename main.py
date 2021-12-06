import sys
import src.Visualization
from time import process_time_ns
from src.Graph import Graph
#import src.playground as pg
from src.IO import read_data, write_data

def calculateTime(begin, end):
  elapsed = end - begin
  time_milliseconds = (elapsed) * 0.001
  time_microseconds = (elapsed) 
  print(f"time: { time_milliseconds }ms - milliseconds | { time_microseconds }μs - microseconds")
  return (time_microseconds, time_microseconds)

def schedule_task(task):
  pass

def schedule_graph(graph):
  pass

def scheduler(listOfDags: list[Graph]):
  pass

def run():
  listOfDags: list[Graph] = read_data("./src/sample.json") # returns a list of graphs
  print(listOfDags)
  begin = process_time_ns()
  scheduler(listOfDags)
  end = process_time_ns()
  time_results = calculateTime(begin, end) # returns a tuple of time results as (microseconds, nanoseconds)
  write_data("./src/output/sample.csv", [], 0, 0, 0, time_results[0])
  
if __name__ == "__main__":
  run()
