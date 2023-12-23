with open("./Day-23/input.in") as file:
  input = [i for i in file.read().strip().split("\n")]

def find_neighbours(grid, row, col):
  neighbours = []

  for r,c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    new_row, new_col = row + r, col + c 
    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] != "#":
      neighbours.append((new_row, new_col))
    
  return neighbours

def get_graph(grid, points, isPart2):
  graph = {point: {} for point in points}
  directions = {
    "^": [(-1, 0)],
    "v": [(1, 0)],
    "<": [(0, -1)],
    ">": [(0, 1)],
    ".": [(-1, 0), (1, 0), (0, -1), (0, 1)],
  }

  for row, col in points:
    stack = [(0, row, col)]
    visited = {(row, col)}

    while stack:
      steps, current_row, current_col = stack.pop(0)

      if steps != 0 and (current_row, current_col) in points:
        graph[(row, col)][(current_row, current_col)] = steps
        continue

      if isPart2: direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
      else: direct = directions[grid[current_row][current_col]]
      
      for r, c in direct:
        new_row, new_col = current_row + r, current_col + c
        
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] != "#" and (new_row, new_col) not in visited:
          stack.append((steps + 1, new_row, new_col))
          visited.add((new_row, new_col))
  
  return graph

def get_longest_path(graph, start, end, visited):
  if start == end: return 0

  max_path = -float("inf")
  
  visited.add(start)
  for point in graph[start]:
    if point not in visited:  max_path = max(max_path, graph[start][point] + get_longest_path(graph, point, end, visited))
  visited.remove(start)

  return max_path

start = (0, input[0].index("."))
end = (len(input)-1, input[-1].index("."))
points1 = [start, end]
points2 = [start, end]

for r, row in enumerate(input):
  for c, char in enumerate(row):
    if char == "#": continue

    neighbours = find_neighbours(input, r, c)
    if len(neighbours) >= 3 or input[r][c] in "^v<>": points2.append((r, c))
    if len(neighbours) >= 3:  points1.append((r, c))
    

graph1 = get_graph(input, points1, False)
graph2 = get_graph(input, points2, True)
print("Solution 1 Running... ")
solution_1 = get_longest_path(graph1, start, end, set())
print("Solution 2 Running... \nMight take a while...")
solution_2 = get_longest_path(graph2, start, end, set())

print ("Answer to Day 23: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)