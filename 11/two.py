with open('input.txt') as f:
    init_layout = f.read().splitlines()

adjacent = [(num1, num2) for num1 in range(-1, 2) for num2 in range(-1, 2) if num1 != 0 or num2 != 0]


# 0, 0 is top left value
def get_value(layout, coords):

    x, y = coords

    if not 0 <= y <= len(layout)-1:
        return "Out of bounds"

    if not 0 <= x <= len(layout[0])-1:
        return "Out of bounds"

    return layout[y][x]


# 0, 0 is top left value
def write_value(layout, coords, overwrite):

    x, y = coords

    row = layout[y]

    row = row[:x] + overwrite + row[x + 1:]

    layout[y] = row


def check_sight(layout, coords, direction):

    while True:
        
        coords = tuple(coords[index] + direction[index] for index in range(2))

        result = get_value(layout, coords)

        if result in ("#", "L"):
            return result
        
        elif result == "Out of bounds":
            return None
        

prev_layout = init_layout.copy()
layout = prev_layout.copy()

while True:

    for y, row in enumerate(prev_layout):
        for x, seat in enumerate(prev_layout[y]):
            
            # taken
            if seat == "#":
                occupied = 0
                for adj_coords in adjacent:
                    
                    if check_sight(prev_layout, (x, y), adj_coords) == "#":
                        occupied += 1
                
                if occupied >= 5:
                    write_value(layout, (x, y), "L")

            # open
            elif seat == "L":
                for adj_coords in adjacent:
                    
                    if check_sight(prev_layout, (x, y), adj_coords) == "#":
                        break
                
                else:
                    write_value(layout, (x, y), "#")

    
    if layout == prev_layout:
        break

    prev_layout = layout.copy()

print('\n'.join(layout))
occupied_seats = 0

for row in layout:

    for seat in row:
        if seat == "#":
            occupied_seats += 1

print(occupied_seats)