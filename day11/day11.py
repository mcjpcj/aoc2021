import numpy as np


def find_adjacent(cell, grid):
    x0, y0 = cell
    adjacent_cells = []
    for row in range(-1, 2):
        for col in range(-1, 2):
            adjacent_cells.append([x0 + row, y0 + col])

    adjacent_cells = [
        [x, y]
        for [x, y] in adjacent_cells
        if x in range(grid.shape[0])
        and y in range(grid.shape[1])
        and (x, y) != (x0, y0)
    ]
    return adjacent_cells


# Part one
with open("input.txt", "r") as file:
    data = [list(line) for line in file.read().splitlines()]
    data = np.array(data, dtype=int)

flash_count = 0
for _ in range(100):
    flashed = np.zeros(data.shape)
    data += 1
    while True:
        flashing = np.argwhere((data > 9) & (flashed == 0))
        if flashing.size == 0:
            break
        adjacent = []
        for flash in flashing:
            adjacent += find_adjacent(flash, data)
            flash_count += 1
            flashed[flash[0], flash[1]] = 1
        for cell in adjacent:
            data[cell[0], cell[1]] += 1
    data[data > 9] = 0
print(flash_count)
# Part two
with open("input.txt", "r") as file:
    data = [list(line) for line in file.read().splitlines()]
    data = np.array(data, dtype=int)

step = 0
while True:
    step += 1
    data += 1
    flashed = np.zeros(data.shape)

    while True:
        flashing = np.argwhere((data > 9) & (flashed == 0))
        if flashing.size == 0:
            break
        adjacent = []
        for flash in flashing:
            adjacent += find_adjacent(flash, data)
            flash_count += 1
            flashed[flash[0], flash[1]] = 1
        for cell in adjacent:
            data[cell[0], cell[1]] += 1

    data[data > 9] = 0
    if np.all(data == 0):
        print(step)
        break
