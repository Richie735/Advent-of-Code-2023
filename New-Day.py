import os
import datetime

day = datetime.datetime.now().strftime("%d")

directory = f"Day-{day:02}"
os.makedirs(directory, exist_ok=True)

with open(os.path.join(directory, f"Day-{day:02}.py"), "w") as f:
    f.write('with open("./Day-{}/input.in") as file:\n'.format(day))
    f.write('  input = [i for i in file.read().strip().split("\\n")]\n\n')
    f.write('solution_1 = 0\n')
    f.write('solution_2 = 0\n\n')
    f.write('print ("Answer to Day {}: \\n Part 1 => ", solution_1, "\\n Part 2 => ", solution_2)'.format(day))


with open(os.path.join(directory, "README.md"), 'w', encoding='utf-8') as f:
    f.write("# 🎄 Day \n\n## Part 1\n\n\n## Part 2\n\n\n## Solution\n\n```\npart-1 => \npart-2 => \n```")

open(os.path.join(directory, "input.in"), 'w').close()
