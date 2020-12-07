with open('input.txt') as f:
    grid = f.read().splitlines()

print("\n".join(grid))

# top left is 0 0
def get_coords_at(x, y):

    row = grid[y]

    while x >= len(row):
        x -= len(row)

    return grid[y][x]

trees = []

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

for slope in slopes:
    x = y = 0
    temp_trees = 0

    while y < len(grid) - 1:
        
        x += slope[0]
        y += slope[1]

        if get_coords_at(x, y) == "#":
            temp_trees += 1

        print(x, y, get_coords_at(x, y))

    trees.append(temp_trees)

total = 1
for amount in trees:
    total *= amount

print(total)