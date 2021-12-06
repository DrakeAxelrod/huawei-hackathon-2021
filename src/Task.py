from dataclasses import dataclass, field
from typing import Any

# reference
@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)

# you want to use the task a a node in the graph
@dataclass()
class Task:
  def __init__(self, taskID, EET, taskType):
    self.id: str = taskID
    # Estimated Execution Time
    self.EET: int = EET
    # task type
    self.type: int = taskType
    # you do not need to represent the tasks dependent as the graph will be able to do that

  # def __hash__(self):
  #   return hash((self.id))

  # def __eq__(self, other):
  #   return (self.id) == (other.id)

  def __str__(self):
    return "<class '%s'>" % self.__class__.__name__ + '\n' + '\n'.join(('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))
