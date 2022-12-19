# https://github.com/Farbfetzen/Advent_of_Code/blob/main/python/2021/day15.py

from collections import defaultdict
import numpy as np
import sys
from queue import PriorityQueue

np.set_printoptions(suppress=True, linewidth=np.nan, threshold=sys.maxsize)

data = [[int(point) for point in row] for row in open('input.txt').read().split('\n')]

original_input = np.array(data)
graph_input = np.array(data)

for i in range(4):
  original_input += 1
  original_input[original_input > 9] = 1
  graph_input = np.concatenate((graph_input, original_input), axis = 1)

original_input = graph_input.copy()
for i in range(4):
  original_input += 1
  original_input[original_input > 9] = 1
  graph_input = np.concatenate((graph_input, original_input), axis = 0)



def manhattan_distance(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_priority_queue(graph, start, end):
  open_list = PriorityQueue()  
  closed_list = {start: None}

  risk_so_far = {start: 0}
  neighbor_offsets = ((1,0), (0,1), (-1,0), (0, -1))
  position = None

  # put the start into the queue
  open_list.put((0, start))
  
  while not open_list.empty():
    # get top priority (lowest risk) node from queue and blacklist it on closed_list
    position = open_list.get()[1]

    # you got to the end
    if position == end:
      break

    # for each neighbor of your current position
    for offset in neighbor_offsets:
      new_position = (position[0] + offset[0], position[1] + offset[1])
      # if the new position is on the map
      if 0 <= new_position[0] < len(graph[0]) and 0 <= new_position[1] < len(graph):
        # calculate the risk level for going into the new position
        new_risk = risk_so_far[position] + graph[new_position[1]][new_position[0]]
        # if the new position is not black listed or presents a lower risk
        print(new_position)
        print(risk_so_far)
        input()
        if new_position not in closed_list or new_risk < risk_so_far[new_position]:
          risk_so_far[new_position] = new_risk
          priority = new_risk + manhattan_distance(new_position, end)
          open_list.put((priority, new_position))
          closed_list[new_position] = position
  
  return risk_so_far[position]

start = (0,0)
x, y = graph_input.shape
end = (x-1, y-1)

# A*
path = a_star_priority_queue(graph_input.tolist(), start, end)
print(path)
