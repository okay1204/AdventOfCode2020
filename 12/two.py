import math

with open('input.txt') as f:
    instructions = f.read().splitlines()


directions = ("N", "E", "S", "W")

# east, north
ship = [0, 0]
waypoint = [10, 1]

def move(oper, value):

    if oper == "N":
        waypoint[1] += value
    elif oper == "E":
        waypoint[0] += value
    elif oper == "S":
        waypoint[1] -= value
    elif oper == "W":
        waypoint[0] -= value

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


for instruction in instructions:

    oper = instruction[0]
    value = int(instruction[1:])

    if oper in directions:
        move(oper, value)
    
    elif oper == "F":

        for index in range(2):
            ship[index] += waypoint[index] * value


    elif oper in ("R", "L"):

        if oper == "R":
            value = 360 - value

        radians = value * math.pi/180

        waypoint = list(rotate((0, 0), waypoint, radians))



print(int(sum([abs(value) for value in ship])))