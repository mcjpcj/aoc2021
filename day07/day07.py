import numpy as np
crabs = np.genfromtxt("input.txt", delimiter=",", dtype=int)
crabs_count = {crab: np.count_nonzero(crabs == crab) for crab in set(crabs)}
# Part one
desired_pos = np.sort(crabs)[crabs.size // 2]
print(np.sum([np.abs(crab_pos - desired_pos) * count for crab_pos, count in crabs_count.items()]))
# Part two
desired_pos = int(np.mean(crabs))
metric = lambda x: int(x * (x + 1) / 2)
print(np.sum([metric(np.abs(crab_pos - desired_pos)) * count for crab_pos, count in crabs_count.items()]))
