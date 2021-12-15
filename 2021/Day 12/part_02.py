from collections import Counter, defaultdict

data = [[point for point in row.split(
    '-')] for row in open('input.txt').read().split('\n')]

haveVisitedTwice = []

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
  global canVisit
  path = path + [start]
  if start == end:
    return [path]
  if start not in graph:
    return []
  paths = []
  for node in graph[start]:
    canVisitThisNode = True
    
    # no going back to the start
    if node == 'start':
      canVisitThisNode = False

    # check for small cave visitability
    # check if any small caves have already been visited twice on this path
    smallCavesOnThisPath = [n for n in path if n.islower() and n != 'start']    
    for k,v in {sc[0]:sc[1] for sc in Counter(smallCavesOnThisPath).most_common()}.items():
      # if a small cave has already been visited twice on this path and the current node
      # we're evaluating is a small cave and is already on this path then you may not visit it
      if v == 2 and Counter(smallCavesOnThisPath)[node] > 0:
        canVisitThisNode = False
    # if you've already been to this small cave twice in another path you may not visit it
    if node in haveVisitedTwice:
      canVisitThisNode = False
    
    if canVisitThisNode:
      newpaths = find_all_paths(graph, node, end, path, visitOnce)
      for newpath in newpaths:
        paths.append(newpath)
    
  return paths

graph = build_graph(data)

paths = find_all_paths(graph, 'start', 'end')

print(len(paths))
