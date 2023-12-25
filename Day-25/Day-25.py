import networkx as nx

with open("./Day-25/input.in") as file:
  input = [i for i in file.read().strip().split("\n")]

graph = nx.Graph()
for line in input:
  source, connections = line.split(":")
  for component in connections.strip().split():
    graph.add_edge(source, component)
    graph.add_edge(component, source)

minimum_edge_cut = nx.minimum_edge_cut(graph)
graph.remove_edges_from(minimum_edge_cut)
componet_a, component_b = nx.connected_components(graph)

solution_1 = len(componet_a) * len(component_b)

print ("Answer to Day 25: \n Part 1 => ", solution_1)