import numpy as np

with open("input.txt", "r") as file:
    data = file.read().splitlines()

# Part one
counter = 0
for line in data:
    input, output = line.split("|")
    output_lengths = np.array([len(i) for i in output.split()])
    counter += np.count_nonzero(
        (output_lengths == 2)
        | (output_lengths == 3)
        | (output_lengths == 4)
        | (output_lengths == 7)
    )
print(counter)
# Part two

digits = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}


def find_wire_map(input):
    wire_map = {}
    input = np.array([set(entry) for entry in input])
    input_lengths = np.array([len(entry) for entry in input])
    wire_map["a"] = input[input_lengths == 3] - input[input_lengths == 2]
    wire_bd = input[input_lengths == 4] - input[input_lengths == 2]
    wire_cf = input[input_lengths == 2]
    wire_eg = input[input_lengths == 7] - input[input_lengths == 4] - wire_map["a"]
    mappings_235 = np.ravel([list(wires) for wires in input[input_lengths == 5]])
    unique, counts = np.unique(mappings_235, return_counts=True)
    wire_be = {x[0] for x in unique[np.argwhere(counts == 1)]}
    wire_map["b"] = wire_bd & wire_be
    wire_map["d"] = wire_bd - wire_map["b"]
    wire_map["e"] = wire_be - wire_map["b"]
    wire_map["g"] = wire_eg - wire_map["e"]
    mappings_9 = wire_cf | wire_map["a"] | wire_map["b"] | wire_map["d"] | wire_map["g"]
    mappings_06 = np.ravel(
        [list(wires) for wires in input[input_lengths == 6] if wires != mappings_9]
    )
    unique, counts = np.unique(mappings_06, return_counts=True)
    wire_cd = {x[0] for x in unique[np.argwhere(counts == 1)]}
    wire_map["c"] = wire_cd - wire_map["d"]
    wire_map["f"] = wire_cf - wire_map["c"]
    return {key: list(val[0])[0] for key, val in wire_map.items()}


def find_digit_map(wire_map):
    digit_map = {}
    for digit, wires in digits.items():
        wires_maped = "".join([wire_map[wire] for wire in wires])
        digit_map["".join(sorted(wires_maped))] = str(digit)
    return digit_map


ans = 0
for line in data:
    input, output = [part.split() for part in line.split("|")]
    wire_map = find_wire_map(input)
    digit_map = find_digit_map(wire_map)
    output = ["".join(sorted(wires)) for wires in output]
    output_digits = [digit_map[wires] for wires in output]
    ans += int("".join(output_digits))
print(ans)
