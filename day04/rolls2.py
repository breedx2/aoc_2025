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

def print_grid(grid):
    for row in grid:
        print(''.join(row))
    print('-'*len(grid[0]))

def clone_grid(grid):
    result = list()
    for row in grid:
        result.append(list(row))
    return result

def mark_grid(input_grid):
    ct = 0
    grid = clone_grid(input_grid)
    for row in range(0, len(input_grid)):
        for col in range(0, len(input_grid[row])):
            if grid_item(input_grid, row, col) == '@':
                neighbors = surrounds(input_grid, row, col)
                # print(neighbors)
                rolls = list(filter(lambda x: x == '@', neighbors))
                if len(rolls) < 4:
                    grid[row][col] = 'x'
                    ct = ct + 1
    return (grid, ct)

sum = 0
grid = list()
for line in stdin:
    grid.append(list(line.strip()))
print_grid(grid)
(marked, ct) = mark_grid(grid)
sum = sum + ct
print_grid(marked)

print(sum)