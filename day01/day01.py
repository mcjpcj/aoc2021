import numpy as np

data = np.loadtxt("input.txt")
# Part one
print(np.count_nonzero(np.diff(data) > 0))
# Part two
window_length = 3
rolling_sum_data = [
    np.sum(data[i : i + window_length]) for i in range(data.size - window_length + 1)
]
print(np.count_nonzero(np.diff(rolling_sum_data) > 0))
