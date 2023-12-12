from collections import deque

with open("./Day-10/input.in") as file:
    input = [i for i in file.read().strip().split("\n")]

num_rows, num_cols = len(input), len(input[0])

directions = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    ".": [],
}

def get_starting_position():
    for i, line in enumerate(input):
        if "S" in line:
            return (i, line.index("S"))
        
def replace_starting_position(i, j):
    if input[i][j] == "S":
        up_valid = (input[i-1][j] in ["|", "7", "F"])
        right_valid = (input[i][j+1] in ["-", "7", "J"])
        down_valid = (input[i+1][j] in ["|", "L", "J"])
        left_valid = (input[i][j-1] in ["-", "L", "F"])
        
        assert sum([up_valid, right_valid, down_valid, left_valid]) == 2

        line = list(input[i])

        if up_valid and down_valid:         line[j] = '|'
        elif up_valid and right_valid:      line[j] = 'L'
        elif up_valid and left_valid:       line[j] = 'J'
        elif down_valid and right_valid:    line[j] = 'F'
        elif down_valid and left_valid:     line[j] = '7'
        elif left_valid and right_valid:    line[j] = '-'
        else:   assert False

        input[i] = ''.join(line)

def get_conected_nodes(i, j):   return directions.get(input[i][j], [])

def get_neighbours(actual_node_i, actual_node_j):
    neighbours = []

    for i, j in list(get_conected_nodes(actual_node_i, actual_node_j)):
        ii, jj = actual_node_i + i, actual_node_j + j

        if not (0 <= ii < num_rows and 0 <= jj < num_cols): continue

        neighbours.append((ii, jj))
    
    return neighbours

def count_double_curves(i, j):
    line = input[i]
    count = 0

    for k in range(j):
        if not (i, k) in visited:   continue
        count += line[k] in ["J", "L", "|"]
        # F - - - J
        # L - - - 7

    return count

start_i, start_j = get_starting_position()
replace_starting_position(start_i, start_j)

visited = set()
distances = {}
queue = deque([((start_i, start_j), 0)])

while queue:
    actual_node, actual_distance = queue.popleft()

    if actual_node in visited: continue

    visited.add(actual_node)
    distances[actual_node] = actual_distance

    for neighbour in get_neighbours(*actual_node):
        if neighbour not in visited:    queue.append((neighbour, actual_distance + 1))

solution_1 = max(distances.values())


visited = set()
stack = [(start_i, start_j)]

while len(stack) > 0:
    top = stack.pop()

    if top in visited: continue

    visited.add(top)

    for neighbour in list(get_neighbours(*top)):
        if neighbour not in visited:    stack.append(neighbour)

solution_2 = 0

# Ray casting algorithm
# tip from: https://www.reddit.com/r/adventofcode/comments/18ft3y3/2023_day_10_part_2_rust_this_has_been_bothering/ 
for i, line in enumerate(input):
    for j in range(num_cols):
        if not (i, j) in visited:   
            double_curves = count_double_curves(i, j)

            if double_curves % 2:  solution_2 += 1

print ("Answer to Day 01: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)