with open("input.txt") as f:
    lines = f.read().splitlines()

correct = 0

for line in lines:
    positions = line.split()[0].split('-')
    positions = list(map(lambda number: int(number)-1, positions))

    letter = line.split(':')[0][-1]

    password = line.split(': ')[1]

    position_count = 0

    for position in positions:
        if position < len(password) and password[position] == letter:
            position_count += 1

    if position_count == 1:
        correct += 1

    print(line)
    print(position_count)
    
print(correct)
