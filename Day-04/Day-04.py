from collections import defaultdict

with open("./Day-04/input.in") as file:
    input = [i for i in file.read().strip().split("\n")]

solution_1 = 0

scratchcards_count = defaultdict(int)

for index, line in enumerate(input):
    first, all_game_numbers = line.split('|')
    card_id, all_winning_numbers = first.split(':')

    game_numbers = [int(i) for i in all_game_numbers.split()]
    winning_numbers = [int(i) for i in all_winning_numbers.split()]
    
    matching_numbers = set(game_numbers) & set(winning_numbers)
    if len(matching_numbers) > 0:
        solution_1 += 2 ** (len(matching_numbers) - 1)

    scratchcards_count[index] += 1
    for i in range(len(matching_numbers)): 
        scratchcards_count[index + 1 + i] += scratchcards_count[index]

solution_2 = sum(scratchcards_count.values())

print ("Answer to Day 04: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)