with open('input.txt') as f:
    xmas_code = f.read().splitlines()

xmas_code = list(map(lambda number: int(number), xmas_code))

for index, number in enumerate(xmas_code[25:]):
    index += 25

    prev = xmas_code[index-25:index]
    
    correct = False
    for add1 in prev:
        for add2 in prev:

            if add1 != add2 and add1 + add2 == number:
                correct = True
                break
        
        if correct:
            break
    else:
        print(number)
        break
        