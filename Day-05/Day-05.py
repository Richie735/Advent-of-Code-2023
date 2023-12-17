with open("./Day-05/input.in") as file:
    input = [i for i in file.read().strip().split("\n")]

seeds = list(map(int, input[0].split(" ")[1:]))
maps = []

seed_ranges = [
    (seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)
]
conversion_maps = []

# Parse Conversion Maps
i = 2 # Skip to third line
while i < len(input):
    maps.append([])

    source_category, _, destination_category = input[i].split(" ")[0].split("-")
    conversion_maps.append([])

    i += 1

    while i < len(input) and not input[i] == "":
        destination_start, source_start, range_length = map(int, input[i].split())
        maps[-1].append((destination_start, source_start, range_length))

        conversion_maps[-1].append((destination_start, source_start, range_length))
        
        i += 1
    
    conversion_maps[-1].sort(key=lambda x: x[1])

    i += 1


def get_location(seed):
    current_number = seed

    for map in maps:
        for destination_start, source_start, range_length in map:
            if source_start <= current_number < source_start + range_length:
                current_number = destination_start + (current_number - source_start)
                break
    
    return current_number

for conversion_map in conversion_maps:
    for i in range(len(conversion_map) - 1):
        if not conversion_map[i][1] + conversion_map[i][2] <= conversion_map[i+1][1]:
            print(conversion_map[i], conversion_map[i + 1])


def remap_interval(start_range, end_range, conv_map):
    remapped_intervals = []

    for destination, source, rangeL in conv_map:
        end = source + rangeL
        shift = destination - source

        if not (end < start_range or source > end_range):
            remapped_intervals.append((max(source, start_range), min(end, end_range), shift))
        
    for i, interval in enumerate(remapped_intervals):
        left, right, shift = interval

        yield (left + shift, right + shift)

    if len(remapped_intervals) == 0:
        yield (start_range, end_range)
        return
    
    if remapped_intervals[0][0] != start_range:
        yield (start_range, remapped_intervals[0][0] - 1)
    if remapped_intervals[-1][1] != end_range:
        yield (remapped_intervals[-1][1] + 1, end_range)
    

locations = []
for seed in seeds: locations.append(get_location(seed))
solution_1 = min(locations)

locations = []
solution_2 = 1 << 60
for start, rangeL in seed_ranges:
    current_intervals = [(start, start + rangeL - 1)]
    new_intervals = []

    for map in conversion_maps:
        for start_range, end_range in current_intervals:
            for new_interval in remap_interval(start_range, end_range, map): new_intervals.append(new_interval)
        
        current_intervals = new_intervals 
        new_intervals = []

    for start_range, end_range in current_intervals:
        solution_2 = min(solution_2, start_range)

print ("Answer to Day 05: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)