import numpy as np


# Part one
lanterfishes = np.genfromtxt("input.txt", delimiter=",", dtype=int)
duration = 80
for day in range(0, duration):
    lanterfishes = lanterfishes - 1
    new_lanterfishes = np.array([8] * np.count_nonzero(lanterfishes == -1), dtype=int)
    lanterfishes = np.append(lanterfishes, new_lanterfishes)
    lanterfishes[lanterfishes == -1] = 6
print(lanterfishes.size)
# Part two
lanterfishes = np.genfromtxt("input.txt", delimiter=",", dtype=int)
duration = 256
memory = {}

def population_count(day, first_gen=False):
    global memory, duration
    try:
        return memory[day]
    except KeyError:
        if first_gen:
            births = np.arange(day, duration, 7)
        else:
            births = np.arange(day + 2, duration, 7)
        count = births.size
        for birth in births[1:]:
            count += population_count(birth)
        memory[day] = count
        return count

print(
    np.sum(list(map(lambda x: population_count(x, first_gen=True), lanterfishes)))
    + lanterfishes.size
)
