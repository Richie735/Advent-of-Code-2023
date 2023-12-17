from heapq import heappop, heappush


with open("./Day-17/input.in") as file:
  input = [i for i in file.read().strip().split("\n")]
input = [[int(char) for char in row] for row in input]


def find_optimal_path(start, end, min_steps, max_straight_steps, matrix, isvalid_part1):
  # Modified version of Dijkstra's algorithm
  # https://en.wikipedia.org/wiki/Dijkstra's_algorithm

  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
  visited = {}
  queue = [(0, start, -1, 0)] #loss, position, direction(no initial direction), straight_steps

  while queue:
    current_loss, current_position, current_direction, straight_steps = heappop(queue)
    if current_position == end: return current_loss

    possible_directions = [d for d in range(4) if d != current_direction and (d + 2) % 4 != current_direction]

    for new_direction in possible_directions:
        new_loss = current_loss

        for straight_steps in range(1, max_straight_steps + 1):
            new_position = tuple(pos + dir * straight_steps for pos, dir in zip(current_position, directions[new_direction]))

            if 0 <= new_position[0] < len(matrix) and 0 <= new_position[1] < len(matrix[0]):
                new_loss += matrix[new_position[0]][new_position[1]]

                if isvalid_part1:
                   if new_loss < visited.get((new_position, new_direction), float("inf")):
                      visited[(new_position, new_direction)] = new_loss
                      
                      if straight_steps >= min_steps: heappush(queue, (new_loss, new_position, new_direction, straight_steps))
                
                else:
                  isvalid_part2 = straight_steps <= 10 and (new_direction == current_direction or straight_steps >= 4 or straight_steps == -1)

                  if new_loss < visited.get((new_position, new_direction), float("inf")) and isvalid_part2:
                      visited[(new_position, new_direction)] = new_loss
                      
                      if straight_steps >= min_steps: heappush(queue, (new_loss, new_position, new_direction, straight_steps))
  return new_loss

solution_1 = find_optimal_path((0, 0), (len(input) - 1, len(input[0]) - 1), 1, 3 , input, True)
solution_2 = find_optimal_path((0,0), (len(input) - 1, len(input[0]) - 1), 4, 10, input, False)

print ("Answer to Day 17: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)
