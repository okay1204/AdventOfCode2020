with open('input.txt') as f:
    grid = f.read().splitlines()

x = y = 0
print("\n".join(grid))

# top left is 0 0
def get_coords_at(x, y):

    row = grid[y]

    while x >= len(row):
        x -= len(row)

    return grid[y][x]

trees = 0
while y < len(grid) - 1:
    
    x += 3
    y += 1

    if get_coords_at(x, y) == "#":
        trees += 1

    print(x, y, get_coords_at(x, y))

print(trees)