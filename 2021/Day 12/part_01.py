from collections import defaultdict
from queue import Queue

data = [[point for point in row.split(
    '-')] for row in open('input.txt').read().split('\n')]

def build_graph(d):
    edges = d
    graph = defaultdict(list)

    for edge in edges:
        a, b = edge[0], edge[1]

        graph[a].append(b)
        graph[b].append(a)

    return graph

# https://stackoverflow.com/questions/24471136/how-to-find-all-paths-between-two-graph-nodes
def find_all_paths(graph, start, end, path=[], visitOnce=['start']):
  path = path + [start]
  if start == end:
    return [path]
  if start not in graph:
    return []
  paths = []
  for node in graph[start]:
    visitOnce = [n for n in path if n.islower()] + ['start']
    if node not in visitOnce:
      newpaths = find_all_paths(graph, node, end, path, visitOnce)
      for newpath in newpaths:        
        paths.append(newpath)
    
  return paths 


graph = build_graph(data)

paths = find_all_paths(graph, 'start', 'end')
print(len(paths))
