with open("./Day-13/input.in") as file:
    input = [i for i in file.read().strip().split("\n\n")]


def find_reflection_line(grid, part_2):
    total_reflections = 0
    rows = len(grid)
    columns = len(grid[0])

    # Check for vertical symmetry
    for col in range(columns - 1):
        dissimilarity = 0
        
        for distance in range(columns):
            left_col = col - distance           
            right_col = col + distance + 1

            if 0 <= left_col < right_col < columns:
                for row in range(rows):
                    if grid[row][left_col] != grid[row][right_col]: dissimilarity += 1
        
        if part_2:
            if dissimilarity == 1:  total_reflections += col + 1
        else:
            if dissimilarity == 0:  total_reflections += col + 1

    # Check for horizontal symmetry
    for row in range(rows - 1):
        dissimilarity = 0
        
        for distance in range(rows):
            top_row = row - distance
            bottom_row = row + distance + 1

            if 0 <= top_row < bottom_row < rows:
                for col in range(columns):
                    if grid[top_row][col] != grid[bottom_row][col]: dissimilarity += 1

        if part_2:  
            if dissimilarity == 1:  total_reflections += 100 * (row + 1)
        else:
            if dissimilarity == 0:  total_reflections += 100 * (row + 1)
    
    return total_reflections


solution_1 = 0
solution_2 = 0
for pattern in input:
    grid = [list(row) for row in pattern.split("\n")]
    solution_1 += find_reflection_line(grid, False)
    solution_2 += find_reflection_line(grid, True)


print ("Answer to Day 13: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)