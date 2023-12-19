from collections import  deque

with open("./Day-19/input.in") as file:
  input = [i for i in file.read().strip().split("\n\n")]

workflows = {}
for line in input[0].split("\n"):
    name, rest = line[:-1].split("{")
    rules = rest.split(",")
    workflows[name] = ([], rules.pop())
    for rule in rules:
      comparison, next = rule.split(":")
      cat = comparison[0]
      check = comparison[1]
      num = int(comparison[2:])
      workflows[name][0].append((cat, check, num, next))

categories = {
  "x": 0,
  "m": 1,
  "a": 2,
  "s": 3,
}

def rating(part):
  rating = 0
  for i in range(4):  rating += part[i]
  return rating

def process_workflow(part, state):
  if state == "R": return False
  elif state == "A": return True
    
  rules, fallback = workflows[state]

  for cat, check, num, next in rules:
    if (check == "<" and part[categories[cat]] < num) or (check == ">" and part[categories[cat]] > num):
      return process_workflow(part, next)

  return process_workflow(part, fallback)



def count(ranges, name = "in"):
  if name == "R": return 0
  if name == "A":
    product = 1
    
    for low, high in ranges.values():
      product *= high - low + 1
    
    return product

  rules, fallback = workflows[name]

  total = 0

  for cat, check, n, next in rules:
    low, high = ranges[cat]
    if check == "<":
        true_range = (low, min(n - 1, high))
        false_range = (max(n, low), high)
    else:
        true_range = (max(n + 1, low), high)
        false_range = (low, min(n, high))
    if true_range[0] <= true_range[1]:
        copy = dict(ranges)
        copy[cat] = true_range
        total += count(copy, next)
    if false_range[0] <= false_range[1]:
        ranges = dict(ranges)
        ranges[cat] = false_range
    else: break
  
  else: total += count(ranges, fallback)

  return total


solution_1 = 0
for part in input[1].split("\n"):
  part = part[1:-1]
  part = [int(x.split("=")[1]) for x in part.split(",")]
  if process_workflow(part, "in"):  solution_1 += rating(part)
  
solution_2 = count({cat: (1, 4000) for cat in "xmas"})


print ("Answer to Day 19: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)