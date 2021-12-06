import sys
from src.Graph import Graph
#import src.playground as pg
from src.Reader import read_data

def run():
  dags: list[Graph] = read_data("./src/sample.json") # returns a list of graphs
  print(dags)
  
if __name__ == "__main__":
  run()
