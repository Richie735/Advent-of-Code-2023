with open("./Day-11/input.in") as file:
    input = [i for i in file.read().strip().split("\n")]

num_rows, num_cols = len(input), len(input[0])
empty_rows = [all([input[i][j] == "." for j in range(num_cols)]) for i in range(num_rows)]
empty_cols = [all([input[i][j] == "." for i in range(num_rows)]) for j in range(num_cols)]


def get_galaxys(galaxy_cords):
    for i in range(num_rows):
        for j in range(num_cols):
            if input[i][j] == "#":  galaxy_cords.append((i, j))

    return galaxy_cords


def get_distance(cord_1, cord_2, expansion_factor):
    i1, j1 = cord_1
    i2, j2 = cord_2

    # Sort Cordinates
    # 1 = smaller, 2 = bigger
    if i1 > i2:     i1, i2 = i2, i1
    if j1 > j2:     j1, j2 = j2, j1

    distance = 0

    for i in range(i1, i2):
        distance += 1
        if empty_rows[i]:   distance += expansion_factor - 1   # Expanding Universe

    for j in range(j1, j2):
        distance += 1
        if empty_cols[j]:   distance += expansion_factor - 1   # Expanding Universe

    return distance
    

galaxy_cords = []
galaxy_cords = get_galaxys(galaxy_cords)

solution_1 = 0
solution_2 = 0
for i in range(len(galaxy_cords)):
    for j in range(i+1, len(galaxy_cords)):
        solution_1 += get_distance(galaxy_cords[i], galaxy_cords[j], 2)
        solution_2 += get_distance(galaxy_cords[i], galaxy_cords[j], 10**6)


print ("Answer to Day 11: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)