from collections import defaultdict

with open("./Day-02/input.in") as file:
    input = [i for i in file.read().strip().split("\n")]

cube_thresholds = {'red': 12, 'green': 13, 'blue': 14}
solution_1 = 0
solution_2 = 0

for line in input:
    possible = True
    id, line = line.split(':')

    dic = defaultdict(int) 
    power = 1

    for event in line.split(';'):
        for balls in event.split(','):
            n,color = balls.split()
            n = int(n)

            dic[color] = max(dic[color], n)

            if int(n) > cube_thresholds[color]: possible = False

    for i in dic.values(): power *= i
    solution_2 += power
    
    if possible: 
        solution_1 += int(id.split()[-1])

print("Answer to Day 02:\nPart 1 =>", solution_1, "\nPart 2 =>", solution_2)