import numpy as np
from scipy import stats
with open("input.txt", "r") as file:
    data = [list(bin_number) for bin_number in file.read().splitlines()]
    data = np.array(data, dtype=int)
# Part one
gamma = "".join(map(str,  stats.mode(data)[0][0]))
epsilon = "".join(map(lambda x: str(int(x) ^ 1), stats.mode(data)[0][0]))
print(int(epsilon, base=2) * int(gamma, base=2))
# Part two
def find_rating(data, co2):
    def eliminate(data, col):
        mode = stats.mode(data[:,col])[0][0]
        count = stats.mode(data[:,col])[1][0]
        if co2:
            mode = not mode
        if count == data.shape[0] - count:
            if co2:
                mode = 0
            else:
                mode = 1
        return data[data[:,col] == mode,:]
        
    for i in range(data.shape[1]):
        data = eliminate(data, i) 
        if data.shape[0] == 1:
            return data[0]
            
oxygen_ratings = "".join(map(str,  find_rating(data, co2=False)))
co2_ratings = "".join(map(str,  find_rating(data, co2=True)))
print(int(oxygen_ratings, base=2) * int(co2_ratings, base=2))

def bin_reversy(binnum):
    return binnum ^ "0xFFFF"

