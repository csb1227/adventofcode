from collections import defaultdict
import numpy as np

data = [[int(point) for point in row] for row in open('input.txt').read().split('\n')]

graph_input = np.array(data)

class Graph():
  def __init__(self):
    self.caves = defaultdict(list)
    self.risks = {}

  def add_edge(self, from_cave, to_cave, risk):
    self.caves[from_cave].append(to_cave)
    self.caves[to_cave].append(from_cave)
    self.risks[(from_cave, to_cave)] = risk
    # self.risks[(to_cave, from_cave)] = risk

def dijsktra(graph, initial, end):
  # shortest paths is a dict of nodes
  # whose value is a tuple of (previous node, weight)
  shortest_paths = {initial: (None, 0)}
  current_node = initial
  visited = set()
  
  while current_node != end:
    visited.add(current_node)
    destinations = graph.caves[current_node]
    weight_to_current_node = shortest_paths[current_node][1]

    for next_node in destinations:
      weight = graph.risks[(current_node, next_node)] + weight_to_current_node
      if next_node not in shortest_paths:
        shortest_paths[next_node] = (current_node, weight)
      else:
        current_shortest_weight = shortest_paths[next_node][1]
        if current_shortest_weight > weight:
          shortest_paths[next_node] = (current_node, weight)
    
    next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
    if not next_destinations:
      return "Route Not Possible"
    # next node is the destination with the lowest weight
    current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
  
  # Work back through destinations in shortest path
  path = []
  while current_node is not None:
    path.append(current_node)
    next_node = shortest_paths[current_node][0]
    current_node = next_node
  # Reverse path
  path = path[::-1]
  return path





# get indices for caves within the cave system
# and get a list of neighbors for each cave
indices = list(np.ndindex(graph_input.shape))
neighbors = defaultdict(list)

for i in indices:
  # for j in [(i[0]-1, i[1]-1), (i[0]-1, i[1]), (i[0]-1, i[1]+1), (i[0], i[1]-1), (i[0], i[1]+1), (i[0]+1, i[1]-1), (i[0]+1, i[1]), (i[0]+1, i[1]+1)]:
  for j in [(i[0]-1, i[1]), (i[0], i[1]-1), (i[0], i[1]+1), (i[0]+1, i[1])]:
    if j in indices:
      neighbors[i].append(j)

# build the graph
graph = Graph()

for i in indices:
  for n in neighbors[i]:
    graph.add_edge(i, n, graph_input[n])

start = (0,0)
x, y = graph_input.shape
end = (x-1, y-1)
path = dijsktra(graph, start, end)

print(sum([graph_input[p] for p in path][1:]))



# 70 wrong