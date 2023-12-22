from collections import deque

with open("./Day-22/input.in") as file:
  input = [i for i in file.read().strip().split("\n")]

def is_overlapping(a, b):
  return max(a[0], b[0]) <= min(a[3], b[3]) and max(a[1], b[1]) <= min(a[4], b[4])

def get_max_z(brick, previous_bricks):
  max_z = 1
  
  for check in previous_bricks:
    if is_overlapping(brick, check):  max_z = max(max_z, check[5] + 1)
  
  return max_z

def adjust_bricks(bricks):
  bricks.sort(key = lambda brick: brick[2])

  for i, brick in enumerate(bricks):
    max_z = get_max_z(brick, bricks[:i])    
    brick[5] -= brick[2] - max_z
    brick[2] = max_z

  bricks.sort(key=lambda brick: brick[2])

def build_support_graph(bricks):
  k_supports_v = {i: set() for i in range(len(bricks))}
  v_supports_k = {i: set() for i in range(len(bricks))}

  for i, upper in enumerate(bricks):
    for j, lower in enumerate(bricks[:i]):
      if is_overlapping(lower, upper) and upper[2] == lower[5] + 1:
        k_supports_v[j].add(i)
        v_supports_k[i].add(j)

  return k_supports_v, v_supports_k

def count_desintegratable(bricks):
  total1, total2 = 0, 0
  k_supports_v, v_supports_k = build_support_graph(bricks)

  for i in range(len(bricks)):
    if all(len(v_supports_k[j]) >= 2 for j in k_supports_v[i]): total1 += 1

    queu = deque(j for j in k_supports_v[i] if len(v_supports_k[j]) == 1)
    falling = set(queu)
    falling.add(i)

    while queu:
      j = queu.popleft()
      for k in k_supports_v[j] - falling:
        if v_supports_k[k] <= falling:
          queu.append(k)
          falling.add(k)

    total2 += len(falling) - 1
  
  return total1, total2

bricks = [list(map(int, line.replace("~", ",").split(","))) for line in input]
adjust_bricks(bricks)
solution_1, solution_2 = count_desintegratable(bricks)

print ("Answer to Day 22: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)