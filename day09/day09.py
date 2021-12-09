import numpy as np
with open("input.txt", "r") as file:
    data = [list(line) for line in file.read().splitlines()]
    heightmap = np.array(data, dtype=int)

# Part one
left_to_right_map = np.diff(heightmap, axis=1, prepend=10) < 0
right_to_left_map = np.flip(np.diff(np.flip(heightmap, axis=1), axis=1, prepend=10), axis=1) < 0
up_to_down_map = np.diff(heightmap, axis=0, prepend=10) < 0
down_to_up_map = np.flip(np.diff(np.flip(heightmap, axis=0), axis=0, prepend=10), axis=0) < 0
low_map = left_to_right_map & right_to_left_map & up_to_down_map & down_to_up_map
print(np.sum(heightmap[low_map] + 1))

# Part two
def visit(point, hmap, visited, to_visit):
    row, col = point
    moves = [(row-1, col), (row +1, col), (row, col-1), (row,col+1)]
    moves = [(row, col) for (row, col) in moves if row in range(0, hmap.shape[0]) and col in range(0, hmap.shape[1])]
    moves = [cords for cords in moves if hmap[cords] != 9 and cords not in visited and cords not in to_visit]
    visited.append(point)
    to_visit += moves
    return to_visit, visited

basin_sizes = []
for low_point in np.argwhere(low_map):
    visited = []
    to_visit = [tuple(low_point)]
    while True:
        if to_visit == []:
            break
        point = to_visit.pop()
        to_visit, visited = visit(point, heightmap, visited, to_visit)
    basin_sizes.append(len(visited))
print(np.prod(sorted(basin_sizes, reverse=True)[:3]))
