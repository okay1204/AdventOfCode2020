with open('input.txt') as f:
    xmas_code = f.read().splitlines()

xmas_code = list(map(lambda number: int(number), xmas_code))

# getting original faulty number
fault_number = None
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
        fault_number = number
        break
        
length = 2

encryption_weakness = None
while True:
    
    for index in range( len(xmas_code)- (length+1) ):

        if sum((portion := xmas_code[index:index+length])) == fault_number:

            encryption_weakness = min(portion) + max(portion)
            break
    
    if encryption_weakness:
        break
        
    length += 1

print(encryption_weakness)
    