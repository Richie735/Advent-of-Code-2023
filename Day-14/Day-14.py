from copy import deepcopy


with open("./Day-14/input.in") as file:
    input = [i for i in file.read().strip().split("\n")]

def roll_north(plataform):
    plataform = [list(row) for row in plataform]

    for c in range(len(plataform[0])):
        for _ in range(len(plataform)):
            for r in range(len(plataform)):
                if plataform[r][c] == "O" and r > 0 and plataform[r-1][c] == ".":
                    plataform[r][c] = "."
                    plataform[r-1][c] = "O"

    plataform = [''.join(row) for row in plataform]

    return plataform

def calculate_load(plataform):
    total_load = 0

    for row in range(len(plataform)):
        for col in range(len(plataform[0])):
            if plataform[row][col] == "O":  total_load += len(plataform) - row

    return total_load

def rotate_clockwise(plataform):
    row_num = len(plataform)
    col_num = len(plataform[0])

    new_plataform = [["?" for _ in range(row_num)] for _ in range(col_num)]

    for row in range(row_num):
        for col in range(col_num):
            new_plataform[col][row_num - row - 1] = plataform[row][col]
            
    return new_plataform

def spin_cycle(plataform, cycles):
    plataform_history = {}
    tilts = 0

    while tilts < cycles:
        tilts += 1

        for direction in range(4):
            plataform = roll_north(plataform)
            
            if tilts == 1 and direction == 0:   plataform_s1 = plataform

            plataform = rotate_clockwise(plataform)

        plat_hash = tuple(tuple(row) for row in plataform)
        if plat_hash in plataform_history: 
            cycle_length = tilts - plataform_history[plat_hash]
            reps = (cycles - tilts) // cycle_length
            tilts += reps * cycle_length
            
        plataform_history[plat_hash] = tilts

    
    return [plataform_s1,plataform]


final_plataform = spin_cycle(deepcopy(input), 10**9)
solution_1 = calculate_load(final_plataform[0])
solution_2 = calculate_load(final_plataform[1])

print ("Answer to Day 14: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)