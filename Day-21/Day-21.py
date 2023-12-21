with open("./Day-21/input.in") as file:
  input = [line.strip() for line in file]

grid = {i + j * 1j: char for i, row in enumerate(input)
  for j, char in enumerate(row) if char in '.S'}

# Lambda function to calculate the number of reachable plots
# Logic form a reddit explanation (don't find the link)
# Couldnt figure out part 2 without it
def calculate_reachable_plots(n, start, step_64, step_65):
  return start + n * (step_64 - start + (n - 1) * (step_65 - step_64 - step_64 + start) // 2)

seen = [] 
reachable_positions = {pos for pos in grid if grid[pos] == 'S'}
apply_modulo = lambda x: complex(x.real % 131, x.imag % 131)

for step in range(3 * 131):
  if step == 64:  solution_1 = len(reachable_positions)
  if step % 131 == 65:    seen.append(len(reachable_positions))

  # Update reachable positions based on movement rules
  reachable_positions = {position + direction for direction in {1, -1, 1j, -1j}
    for position in reachable_positions if apply_modulo(position + direction) in grid}

solution_2 = calculate_reachable_plots(26501365 // 131, *seen)

print ("Answer to Day 21: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)