from sys import stdin

def grid_item(grid, row, col):
    if row < 0 or row >= len(grid):
        return '!'
    the_row = grid[row]
    if col < 0 or col >= len(the_row):
        return '!'
    return the_row[col]

def surrounds(grid, row, col):
    result = [
        grid_item(grid, row-1, col-1),
        grid_item(grid, row+0, col-1),
        grid_item(grid, row+1, col-1),
        grid_item(grid, row-1, col),
        grid_item(grid, row+1, col),
        grid_item(grid, row-1, col+1),
        grid_item(grid, row+0, col+1),
        grid_item(grid, row+1, col+1),
    ]
    return result

grid = list()
for line in stdin:
    grid.append(line.strip())
# print(grid)

ct = 0
for row in range(0, len(grid)):
    for col in range(0, len(grid[row])):
        if grid_item(grid, row, col) == '@':
            neighbors = surrounds(grid, row, col)
            print(neighbors)
            rolls = list(filter(lambda x: x == '@', neighbors))
            if len(rolls) < 4:
                ct = ct + 1

print(ct)