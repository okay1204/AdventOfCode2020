import functools

with open('input.txt') as f:
    adapters = f.read().splitlines()

adapters = list(map(lambda number: int(number), adapters))
adapters.sort()

# wall outlet thing
adapters.insert(0, 0)

# decorator does some magic that just makes recursive functions faster somehow idk
@functools.lru_cache()

def find_arrangements(index):

    # if index has reached end, then return 1
    if index == len(adapters) - 1:
        return 1

    arrangements = 0
    next_index = index + 1

    # if next index is smaller than list, and difference between two adapters is smaller or equal to than 3
    while next_index < len(adapters) and adapters[next_index] - adapters[index] <= 3:
        arrangements += find_arrangements(next_index)
        next_index += 1

    return arrangements

print(find_arrangements(0))