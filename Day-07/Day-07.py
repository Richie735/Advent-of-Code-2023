from collections import defaultdict
from functools import cmp_to_key  

with open("./Day-07/input.in") as file:
    input = [i for i in file.read().strip().split("\n")]

strength = "AKQJT98765432"
joker_strength = "AKQT98765432J"

def get_hand_type(hand):
    counts = defaultdict(int)
    for card in hand:
        counts[card] += 1
    
    amount = sorted(counts.values())
    
    switch_cases = {
        (5,): 6, # Five of a kind
        (1, 4): 5, # Four of a kind
        (2, 3): 4, # Full house
        (1, 1, 3): 3, # Three of a kind
        (1, 2, 2): 2, # Two pairs
        (1, 1, 1, 2): 1 # One pair
    }

    return switch_cases.get(tuple(amount), 0)

def get_joker_hand_type(hand): 
    counts = defaultdict(int)
    jokers = 0
    for card in hand:
        if card == "J": jokers += 1
        else: counts[card] += 1
    
    amount = sorted(counts.values())
    if jokers >= 5 or amount[-1] + jokers >= 5: return 6 # Five of a kind
    if jokers >= 4 or amount[-1] + jokers >= 4: return 5 # Four of a kind

    if amount[-1] + jokers >= 3:
        remaining_jokers = amount[-1] + jokers - 3
        if len(amount) >= 2 and amount[-2] + remaining_jokers >= 2 or remaining_jokers >= 2: return 4 # Full house
        return 3 # Three of a kind

    if amount[-1] + jokers >= 2:
        remaining_jokers = amount[-1] + jokers - 2
        if len(amount) >= 2 and amount[-2] + remaining_jokers >= 2 or remaining_jokers >= 2: return 2 # Two pairs
        return 1 # One pair
    
    return 0

def compare_hands(hand_A, hand_B, isJoker):
    if isJoker:
        rank_A = (get_joker_hand_type(hand_A), hand_A)
        rank_B = (get_joker_hand_type(hand_B), hand_B)
    else:
        rank_A = (get_hand_type(hand_A), hand_A)
        rank_B = (get_hand_type(hand_B), hand_B)
    
    if rank_A[0] == rank_B[0]: 
        if hand_A == hand_B: return 0

        for i, j in zip(hand_A, hand_B):
            if isJoker:
                if joker_strength.index(i) < joker_strength.index(j):
                    return 1
                if joker_strength.index(i) > joker_strength.index(j):
                    return -1
            else:
                if strength.index(i) < strength.index(j):
                    return 1
                if strength.index(i) > strength.index(j):
                    return -1
        
        return -1
    
    if rank_A[0] > rank_B[0]: return 1

    return -1


hands = []
for line in input:
    line = line.split(" ")
    hands.append((line[0], int(line[1])))

hands = sorted(hands, key=cmp_to_key(lambda x, y: compare_hands(x[0], y[0], False)))
solution_1 = 0
for i, line in enumerate(hands): solution_1 += (i + 1) * line[1]

joker_hands = sorted(hands, key=cmp_to_key(lambda x, y: compare_hands(x[0], y[0], True)))
solution_2 = 0
for i, line in enumerate(joker_hands): solution_2 += (i + 1) * line[1]

print ("Answer to Day 07: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)