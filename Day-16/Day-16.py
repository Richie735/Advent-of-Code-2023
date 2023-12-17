with open("./Day-16/input.in") as file:
  input = [i for i in file.read().strip().split("\n")]

def reflect(mirror, direction, x, y):
  if mirror == "/":
    reflection = {
      (0, 1): (-1, 0),  # down to left
      (0, -1): (1, 0),  # up to right
      (1, 0): (0, -1),  # right to up
      (-1, 0): (0, 1)   # left to down
    }
  elif mirror == "\\":
    reflection = {
      (0, 1): (1, 0),   # down to right
      (0, -1): (-1, 0), # up to left
      (1, 0): (0, 1),   # right to down
      (-1, 0): (0, -1)  # left to up
    }

  direction = reflection[direction]
  x += direction[0]
  y += direction[1]

  return x, y, direction

def get_energized(stack):
  visited = set()
  energized = set()

  while stack:
    current_x, current_y, directions = stack.pop()

    while 0 <= current_x < len(input[0]) and 0 <= current_y < len(input):
      current_position = (current_x, current_y, directions)

      if current_position in visited:
        break

      visited.add(current_position)
      energized.add((current_x, current_y))

      match input[current_y][current_x]:
        case ".":
          current_x += directions[0]
          current_y += directions[1]

        case "-":
          if directions[0]:
            current_x += directions[0]
            continue

          stack.append((current_x - 1, current_y, (-1, 0))) # left
          stack.append((current_x + 1, current_y, (1, 0)))  # right
          break

        case "|":
          if directions[1]:
            current_y += directions[1]
            continue

          stack.append((current_x, current_y - 1, (0, -1))) # up
          stack.append((current_x, current_y + 1, (0, 1)))  # down
          break

        case "/": current_x, current_y, directions = reflect("/", directions, current_x, current_y)

        case "\\":  current_x, current_y, directions = reflect("\\", directions, current_x, current_y)
          

  return len(energized)


solution_1 = get_energized([(0, 0, (1, 0))])

solution_2 = 0
for row in range(len(input)):
  solution_2 = max(solution_2, get_energized([(row, 0, (0, 1))]))
  solution_2 = max(solution_2, get_energized([(row, len(input[0]) - 1, (0, -1))]))
for col in range(len(input[0])):
  solution_2 = max(solution_2, get_energized([(0, col, (1, 0))]))
  solution_2 = max(solution_2, get_energized([(len(input) - 1, col, (-1, 0))]))

print ("Answer to Day 16: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)