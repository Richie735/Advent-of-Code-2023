with open("./Day-01/input.in") as file:
    input = [i for i in file.read().strip().split("\n")]

solution_1 = 0
solution_2 = 0

for line in input:
    numbers = []
    numbers2 = []

    for i,char in enumerate(line):
        if char.isdigit():
            numbers.append(char)
            numbers2.append(char)
        
        for j, value in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(value):
                numbers2.append(str(j+1))

    solution_1 += int(numbers[0] + numbers[-1])
    solution_2 += int(numbers2[0] + numbers2[-1])

print ("Answer to Day 01: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)