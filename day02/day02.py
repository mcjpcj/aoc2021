import numpy as np
data = np.loadtxt("input.txt", dtype="str")
# Part one
horizontal_pos = np.sum(data[data[:,0] == "forward", 1].astype(int))
vertical_pos =  np.sum(data[data[:,0] == "down", 1].astype(int)) - np.sum(data[data[:,0] == "up", 1].astype(int))
print(vertical_pos * horizontal_pos)
# Part two
aim, vertical_pos = 0, 0
horizontal_pos = np.sum(data[data[:,0] == "forward", 1].astype(int))
for row in data.tolist():
    match row:
        case ["forward", val]:
            vertical_pos += aim * int(val)
        case ["up", val]:
            aim -= int(val)
        case ["down", val]:
            aim += int(val)
print(vertical_pos * horizontal_pos)