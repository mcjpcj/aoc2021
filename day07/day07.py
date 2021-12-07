import numpy as np
crabs = np.genfromtxt("input.txt", delimiter=",", dtype=int)

crabs_count = {crab: np.count_nonzero(crabs == crab) for crab in set(crabs)}
# Part one
costs = []
for desired_pos in range(0, max(crabs)):
    costs.append(np.sum([np.abs(crab_pos - desired_pos) * count for crab_pos, count in crabs_count.items()]))
print(min(costs))
# Part two
costs = []
dists = {d: d * (d +1 ) / 2 for d in range(min(crabs),max(crabs)+1)}
for desired_pos in range(0, max(crabs)):
    costs.append(np.sum([dists[np.abs(crab_pos - desired_pos)] * count for crab_pos, count in crabs_count.items()]))
print(min(costs))
