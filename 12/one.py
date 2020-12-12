with open('input.txt') as f:
    instructions = f.read().splitlines()


directions = ("N", "E", "S", "W")

north = east = 0

facing = "E"

def move(oper, value):
    global north, east

    if oper == "N":
        north += value
    elif oper == "E":
        east += value
    elif oper == "S":
        north -= value
    elif oper == "W":
        east -= value

for instruction in instructions:

    oper = instruction[0]
    value = int(instruction[1:])

    if oper in directions:
        move(oper, value)
    
    elif oper == "F":
        move(facing, value)

    elif oper in ("R", "L"):

        if oper == "L":
            value = 360 - value
        
        turn_amount = value // 90

        dir_index = directions.index(facing) + turn_amount

        if dir_index > len(directions) - 1:
            dir_index -= len(directions)

        facing = directions[dir_index]

    
print(abs(north) + abs(east))