with open("input.txt") as f:
    lines = f.read().splitlines()

correct = 0

for line in lines:
    lower, upper = line.split()[0].split('-')
    lower = int(lower)
    upper = int(upper)

    letter = line.split(':')[0][-1]

    password = line.split(': ')[1]
    
    count = password.count(letter)

    if lower <= count <= upper:
        correct += 1

print(correct)
