from collections import defaultdict
import re
import math

with open("./Day-08/input.in") as file:
    input = [i for i in file.read().strip().split("\n")]


child_nodes = defaultdict(str)
for line in input[2:]:
    parent, left_child, right_child = re.search("(...) = \((...), (...)\)", line).groups(0)
    child_nodes[parent] = (left_child, right_child)

instructions = input[0]

def single_path_counter(starting_node, ending_node):
    current_node = starting_node
    step_counter = 0
    
    while current_node != ending_node:
        if instructions[step_counter % len(instructions)] == "L": current_node = child_nodes[current_node][0]
        else: current_node = child_nodes[current_node][1]
        step_counter += 1
    
    return step_counter

solution_1 = single_path_counter("AAA", "ZZZ")


def multiple_paths_counter(node): 
    step_counter = 0

    while node[-1] != "Z":
        if instructions[step_counter % len(instructions)] == "L": node = child_nodes[node][0]
        else: node = child_nodes[node][1]

        step_counter += 1

    return step_counter


starting_nodes = [node for node in child_nodes if node[-1] == "A"]
steps = [multiple_paths_counter(node) for node in starting_nodes]
solution_2 = math.lcm(*steps) # common multiple of steps


print ("Answer to Day 01: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)