with open("./Day-09/input.in") as file:
    input = [i for i in file.read().strip().split("\n")]

def step_difference(line): return [line[i + 1] - line[i] for i in range(len(line) - 1)]

def predict (History):
    hist = [History]

    while not all([i == 0 for i in hist[-1]]):
        hist.append(step_difference(hist[-1]))
    
    hist[-1].append(0)
    for i in range(len(hist) - 2, -1, -1):
        hist[i].append(hist[i][-1] + hist[i + 1][-1])

    return hist[0][-1] 


right_history = []
left_history = []
for line in input:
    right_history.append(predict(list(map(int, line.split()))))
    left_history.append(predict(list(map(int, line.split()[::-1]))))

solution_1 = sum(right_history)
solution_2 = sum(left_history)

print ("Answer to Day 01: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)