with open('input.txt') as f:
    boot_code = f.read().splitlines()



def execute(boot_code):

    lines_ran = []

    accumulator = 0
    line_number = 0
    while True:

        # if program finished
        if line_number >= len(boot_code):
            return accumulator

        line = boot_code[line_number]

        oper, arg = line.split()
        arg = int(arg)

        # checking if ran again
        if line_number in lines_ran:
            return False

        lines_ran.append(line_number)

        if oper == "acc":
            accumulator += arg
        elif oper == "jmp":
            line_number += arg
            continue
        elif oper == "nop":
            pass
        
        line_number += 1


# first getting initial lines
lines_ran = []
accumulator = 0
line_number = 0
while True:

    line = boot_code[line_number]

    oper, arg = line.split()
    arg = int(arg)

    # checking if ran again
    if line_number in lines_ran:
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


# then testing different operator changes
for line_number in lines_ran:

    boot_code_copy = boot_code.copy()

    line = boot_code_copy[line_number]

    oper, arg = line.split()

    if oper == "jmp":
        oper = "nop"
    
    elif oper == "nop":
        oper = "jmp"

    boot_code_copy[line_number] = ' '.join((oper, arg))

    return_value = execute(boot_code_copy)
    if return_value:
        print(return_value)
        break