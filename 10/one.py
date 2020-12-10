with open('input.txt') as f:
    adapters = f.read().splitlines()

adapters = list(map(lambda number: int(number), adapters))
adapters.sort()

# for device's adapter
adapters.append(max(adapters) + 3)

differences = {
    1: 0,
    2: 0,
    3: 0
}

prev = 0
for adapter in adapters:

    differences[adapter-prev] += 1

    prev = adapter

print(differences[1] * differences[3])