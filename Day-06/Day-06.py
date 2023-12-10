with open("./Day-06/input.in") as file:
    input = [i for i in file.read().strip().split("\n")]

def getWays(time, distance):
    count = 0

    for i in range(time):
        if (time - i) * i > distance:   count += 1
    
    return count


times = list(map(int, input[0].split()[1:]))
distances = list(map(int, input[1].split()[1:]))

Time = int("".join(input[0].split()[1:]))
Distance = int("".join(input[1].split()[1:]))


possible_options = []
for time, distance in zip(times, distances):
    possible_options.append(getWays(time, distance))

solution_1 = 1
for i in possible_options:  solution_1 *= i

solution_2 = getWays(Time, Distance)

print ("Answer to Day 01: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)