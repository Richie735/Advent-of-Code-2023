from collections import deque
import math


with open("./Day-20/input.in") as file:
  input = [i for i in file.read().strip().split("\n")]

class Module:
  def __init__(self, name, type, outputs):
    self.name = name
    self.type = type
    self.outputs = outputs

    if type == "&": self.memory = {}  # 0 = No pulse, 1 = Low pulse, 2 = High pulse
    elif type == "%": self.memory = False

  def init_memory(self, name):
    if self.type  == "&": self.memory[name] = 1

  def reset(self):
    if self.type == "&": self.memory = {name: 1 for name in self.memory}
    elif self.type == "%": self.memory = False

  def process_pulse(self, origin, pulse, queue):
    if self.type == "%":  self.process_flip_flop(pulse, queue)
    elif self.type == "&": self.process_conjunction(origin, pulse, queue)

  def process_flip_flop(self, pulse, queue):
    if pulse == 1:
      self.memory = not self.memory

      output = 2 if self.memory else 1
      for module in self.outputs: queue.append((self.name, module, output))

  def process_conjunction(self, origin, pulse, queue):
    self.memory[origin] = pulse

    output = 1 if all(pulse == 2 for pulse in self.memory.values()) else 2
    for module in self.outputs: queue.append((self.name, module, output))



modules = {}
# parse input
for line in input:
  l, r = line.split(" -> ")
  outputs = r.split(", ")

  if l == "broadcaster":  modules["broadcaster"] = Module("broadcaster", "broadcaster", outputs)
  else:
    type = l[0]
    name = l[1:]
    modules[name] = Module(name, type, outputs)

# initialize conjunction modules memory
for name, module in modules.items():
  for output in module.outputs:
    if output in modules: modules[output].init_memory(name)



low_pulses = high_pulses = 0
for i in range(1000):
  low_pulses += 1
  queue = deque([("broadcaster", x, 1) for x in modules["broadcaster"].outputs])
  while queue:
    origin, target, pulse = queue.popleft()

    if pulse == 1: low_pulses += 1
    elif pulse == 2: high_pulses += 1

    if target not in modules: continue

    modules[target].process_pulse(origin, pulse, queue)
solution_1 = low_pulses * high_pulses

for name, module in modules.items(): module.reset()

presses = 0
prev_rx, = [name for name, module in modules.items() if "rx" in module.outputs]
seen = {name: 0 for name, module in modules.items() if prev_rx in module.outputs}
cycle = {}
done = False

while True:
  presses += 1
  pulse_queue = deque([("broadcaster", x, 1) for x in modules["broadcaster"].outputs])

  while pulse_queue:
    origin, target, pulse = pulse_queue.popleft()

    if target not in modules: continue

    module = modules[target]

    if module.name == prev_rx and pulse == 2:
      seen[origin] += 1
      
      if origin not in cycle: cycle[origin] = presses
      else: assert presses == seen[origin] * cycle[origin]

      if all(seen.values()):
        solution_2 = 1

        for length in cycle.values():
          solution_2 = solution_2 * length // math.gcd(solution_2, length)
        done = True
        break
      
    modules[target].process_pulse(origin, pulse, pulse_queue) 
    
  if done: break  # This line is indented to be inside the outer while loop

print ("Answer to Day 20: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)