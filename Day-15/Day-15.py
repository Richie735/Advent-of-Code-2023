with open("./Day-15/input.in") as file:
    input = [i for i in file.read().strip().split(",")]

def hash_algorithm(init_sequence):
    current_value = 0

    for char in init_sequence:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    
    return current_value

def calculate_focal_power(boxes):
    total = 0

    for i, box in enumerate(boxes):
        for j, (name, focal_length) in enumerate(box):  
            total += (i + 1) * (j + 1) * focal_length
            print (i, j, focal_length, total)

    return total

solution_1 = 0
for step in input:  solution_1 += hash_algorithm(step)

boxes = [[] for _ in range(256)]
for cmd in input:
    if cmd.endswith("-"): 
        label = cmd[:-1]
        hash = hash_algorithm(label)
        boxes[hash] = [(l, h) for (l, h) in boxes[hash] if l != label]
    
    elif cmd[-2] == "=":
        label = cmd[:-2]
        hash = hash_algorithm(label)
        focal_length = int(cmd[-1])

        if label in [l for (l, h) in boxes[hash]]:  boxes[hash] = [(l, focal_length if label == l else h) for (l, h) in boxes[hash]]
        else: boxes[hash].append((label, focal_length))

solution_2 = calculate_focal_power(boxes)

print ("Answer to Day 15: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)