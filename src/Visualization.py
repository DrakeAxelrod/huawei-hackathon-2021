# Importing the matplotlib.pyplot
import matplotlib.pyplot as plt

def create_task_gant():
  # Declaring a figure "gnt"
  fig, gnt = plt.subplots()
  # Setting Y-axis limits
  gnt.set_ylim(0, 50)
  # Setting X-axis limits
  gnt.set_xlim(0, 160)
  # Setting labels for x-axis and y-axis
  gnt.set_xlabel('microseconds since start')
  gnt.set_ylabel('Processors')
  # Setting ticks on y-axis
  gnt.set_yticks([15, 25, 35])
  # Labelling tickes of y-axis
  gnt.set_yticklabels(['PN1', 'PN2', 'PN3'])
  # Setting graph attribute
  gnt.grid(True)
  # Declaring a bar in schedule
  gnt.broken_barh([(40, 50)], (30, 9), facecolors =('tab:orange'))
  # Declaring multiple bars in at same level and same width
  gnt.broken_barh([(110, 10), (150, 10)], (10, 9),
                          facecolors ='tab:blue')
  gnt.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
                                    facecolors =('tab:red'))
  plt.savefig("./src/output/visual.png")

create_task_gant()
