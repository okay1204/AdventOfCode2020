with open('input.txt') as f:
    numbers = f.read().splitlines()

numbers = list(map(lambda number: int(number), numbers))

for n1 in numbers:
    for n2 in numbers:
        if n1 + n2 == 2020:
            print(n1, n2)
            print(n1 * n2)
            exit()