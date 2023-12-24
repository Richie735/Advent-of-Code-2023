import sympy

with open("./Day-24/input.in") as file:
  input = [i for i in file.read().strip().split("\n")]

def get_slope_n_intercept(coords, velocity):
  x1, y1, z1 = coords
  x2, y2, z2 = x1 + velocity[0], y1 + velocity[1], z1 + velocity[2]
  slope = (y2 - y1) / (x2 - x1)
  intercept = y1 - slope * x1

  return (coords, velocity, slope, intercept)

def will_reach_next_step(coords, velocity, x, y):
  return abs(coords[0] + velocity[0] - x) <= abs(coords[0] - x) and abs(coords[1] + velocity[1] - y) <= abs(coords[1] - y)

min = 200000000000000
max = 400000000000000

hailstones = []
for line in input:
  coords, velocity = line.split("@")
  coords = list(map(int, coords.split(",")))
  velocity = list(map(int, velocity.split(",")))
  hailstones.append(get_slope_n_intercept(coords, velocity))


solution_1 = 0
for i, hail1 in enumerate(hailstones):
  for hail2 in hailstones[i + 1:]:
    if hail1[2] == hail2[2]:  continue

    x = (hail2[3] - hail1[3]) / (hail1[2] - hail2[2])
    y = hail1[2] * x + hail1[3]

    if x < min or x > max or y < min or y > max:  continue
    if will_reach_next_step(hail1[0], hail1[1], x, y) and will_reach_next_step(hail2[0], hail2[1], x, y): solution_1 += 1

xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")
equations = []

for i, (coords, velocity, _, _) in enumerate(hailstones):
  dx, dy, dz = coords
  vx, vy, vz = velocity
  equations.append((xr - dx) * (vy - vyr) - (yr - dy) * (vx - vxr))
  equations.append((yr - dy) * (vz - vzr) - (zr - dz) * (vy - vyr))
  if i < 2: continue  # You need at least 3 equations

  solution = [s for s in sympy.solve(equations) if all(x % 1 == 0 for x in s.values())] 
  if len(solution) == 1:
    break

solution_2 = solution[0][xr] + solution[0][yr] + solution[0][zr]

print ("Answer to Day 24: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)