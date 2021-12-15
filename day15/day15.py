import numpy as np
from itertools import permutations

def get_input(file_name):
    with open(file_name, "r") as file:
        data = [list(line) for line in file.read().splitlines()]
    return np.array(data, dtype=int)

def find_risk(data):
    data = np.flip(data).copy()
    paths = data.copy()
    indcies = []
    dim = data.shape[0]

    for i in range(2, 2 * (dim+1)):
        idx = []
        for up, down in zip(np.arange(0, i, 1), np.arange(i, 0,  -1)):
            if up < dim and (down - 1) < dim:
                idx.append((up, down-1))
        indcies += sorted(idx, key=lambda cord: cord[1])

    for row, col in indcies:
        neighbours = [pair for pair in [(row-1, col), (row, col-1)] if -1 not in pair]
        self_risk = paths[row, col]
        path_risk = min([paths[coords[0], coords[1]] for coords in neighbours])
        for n_row, n_col in neighbours:
            if data[n_row, n_col] + self_risk + path_risk < paths[n_row, n_col]:
                paths[n_row, n_col] = data[n_row, n_col] + self_risk + path_risk
        path_risk = min([paths[coords[0], coords[1]] for coords in neighbours])
        paths[row, col] += path_risk
    return paths[-1, -1] - data[-1,-1]

def get_full_map(data):
    dim = data.shape[0]
    factor = 5
    data = np.tile(data, (factor, factor))
    for i in range(0, factor * dim, dim):
        iter = int(i / dim)
        data[:,i:i+dim] += 1 * iter
        data[i:i+dim,:] += 1 * iter
        data[data > 9] -= 9
    return data

# Part one
data = get_input("test.txt")
print(find_risk(data))
#
# Part two
data = get_input("test.txt")
data = get_full_map(data)
print(find_risk(data))
