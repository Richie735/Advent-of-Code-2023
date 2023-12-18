with open("./Day-18/input.in") as file:
  input = [i for i in file.read().strip().split("\n")]

directions = {
  "U": (-1, 0),
  "D": (1, 0),
  "L": (0, -1),
  "R": (0, 1)
}

def get_size(border, perimeter):
  x_coord, y_coord = zip(*border)
  # Shoelace formula
  # https://en.wikipedia.org/wiki/Shoelace_formula
  left_sum = sum(a * b for a, b in zip(x_coord, y_coord[1:]))
  right_sum = sum(a * b for a, b in zip(y_coord, x_coord[1:]))
    

  # Calculate the area and add the boundary length
  area = abs(left_sum - right_sum) // 2
  total_capacity = area + perimeter // 2 + 1
    
  return total_capacity

def get_lagoon(dig_plan, rgb):
  current_position = (0, 0)
  border = [current_position]
  perimeter = 0

  for line in dig_plan:
    if rgb:
      direction = "RDLU"[int(line[2][-1])]
      steps = int(line[2][1:-1], 16)
      line = (direction, steps, line[2])  # Create a new tuple with updated values

    for _ in range(line[1]):
        current_position = tuple(a + b for a, b in zip(current_position, directions[line[0]]))
        border.append(current_position)
    perimeter += line[1]

  return get_size(border, perimeter)


dig_plan = []
for line in input:
  direction, steps, rgb = line.split(" ")
  rgb = rgb.replace("(", "").replace(")", "")
  dig_plan.append((direction, int(steps), rgb))

solution_1 = get_lagoon(dig_plan, False)
solution_2 = get_lagoon(dig_plan, True)

print ("Answer to Day 18: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)