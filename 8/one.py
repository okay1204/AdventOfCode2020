with open('input.txt') as f:
    boot_code = f.read().splitlines()

lines_ran = []

accumulator = 0
line_number = 0
while True:

    line = boot_code[line_number]

    oper, arg = line.split()
    arg = int(arg)

    # checking if ran again
    if line_number in lines_ran:
        print(accumulator)
        break
    lines_ran.append(line_number)

    if oper == "acc":
        accumulator += arg
    elif oper == "jmp":
        line_number += arg
        continue
    elif oper == "nop":
        pass
    
    line_number += 1