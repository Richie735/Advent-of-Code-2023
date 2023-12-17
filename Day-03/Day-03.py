from collections import defaultdict

with open("./Day-03/input.in") as file:
    input = [i for i in file.read().strip().split("\n")]

solution_1 = 0
solution_2 = 0

Grid = [[char for char in line] for line in input]
Row = len(Grid)
Col = len(Grid[0])

numbers = defaultdict(list)

for row in range(len(Grid)):
    current_number = 0
    is_part = False

    gears = set()

    for col in range(len(Grid[row]) + 1):
        if col<Col and Grid[row][col].isdigit():
            current_number = current_number*10+int(Grid[row][col])
            for row_offset in [-1, 0, 1]:
                for col_offset in [-1, 0, 1]:
                    if 0 <= row + row_offset < Row and 0 <= col + col_offset < Col:
                        char_offset = Grid[row + row_offset][col + col_offset]

                        if not char_offset.isdigit() and char_offset != '.':
                            is_part = True

                        if char_offset == '*':
                            gears.add((row + row_offset, col + col_offset))
        
        elif current_number > 0:
            if is_part: solution_1 += current_number
            
            for gear in gears:
                numbers[gear].append(current_number)
            
            current_number = 0
            is_part = False
            gears = set()

for key, value in numbers.items():
    if len(value) == 2:
        solution_2 += value[0]*value[1]

print ("Answer to Day 03: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)