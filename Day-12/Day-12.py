import functools
with open("./Day-12/input.in") as file:
    input = [line for line in file.read().strip().split("\n")]

def match_beginning(data, length):
    return all(x > 0 for x in data[:length]) and (
        (len(data) == length) or data[length] < 2
    )


@functools.cache
def count_possible_arrangements(data, clusters):
    total = sum(clusters)
    min = sum(x == 2 for x in data)
    max = sum(x > 0 for x in data)

    if min > total or max < total:  return 0
    if total == 0:  return 1
    if data[0] == 0:    return count_possible_arrangements(data[1:], clusters)
    if data[0] == 2:
        length = clusters[0]
        if match_beginning(data, length):
            if length == len(data):  return 1
            return count_possible_arrangements(data[length + 1 :], clusters[1:])
        return 0
    return count_possible_arrangements(data[1:], clusters) + count_possible_arrangements((2,) + data[1:], clusters)

symbol_meaning = {
    ".": 0,     # Operational
    "?": 1,     # Unknown
    "#": 2,     # Broken
}

records = []

for row in input:
    s, c = row.strip().split(" ")
    symbols = tuple(symbol_meaning[i] for i in s)
    clusters = tuple(map(int, c.split(",")))
    records.append((symbols, clusters))

solution_1 = sum(count_possible_arrangements(*line) for line in records)
solution_2 = sum(count_possible_arrangements(((c + (1,)) * 5)[:-1], cluster * 5) for c, cluster in records )

print ("Answer to Day 01: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)