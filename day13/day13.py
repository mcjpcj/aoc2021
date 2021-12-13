import numpy as np

def prepare_data(input):
    with open(input, "r") as file:
        data = file.read().splitlines()
    instructions = data[data.index("")+1:]
    coords = [(int(coord.split(",")[0]), int(coord.split(",")[1])) for coord in data[:data.index("")]]
    max_cols = max([coord[0] for coord in coords])
    max_rows = max([coord[1] for coord in coords])
    paper = np.zeros((max_rows+1, max_cols+1), dtype=int)
    for col, row in coords:
        paper[row, col] = 1
    return paper, instructions

def fold(paper, instruction):
    fold_axis, fold_idx = instruction.split()[-1].split("=")
    fold_idx = int(fold_idx)
    if fold_axis == "y":
        static_paper = paper[:fold_idx, :].copy()
        folded_paper = np.flip(paper[fold_idx+1:, :].copy(), axis=0)
        return static_paper + folded_paper
    elif fold_axis == "x":
        static_paper = paper[:,:fold_idx].copy()
        folded_paper = np.flip(paper[:,fold_idx+1:].copy(), axis=1)
        return static_paper + folded_paper

def uncode_paper(paper):
    ans = ""
    for idx, value in enumerate(paper.flatten()):
        ans += "{}{}".format("\n" if idx % paper.shape[1] == 0 else "", "#" if value else " ")
    return ans

# Part one
paper, instructions = prepare_data("input.txt")
paper = fold(paper, instructions[0])
print(np.count_nonzero(paper))
# Part two
paper, instructions = prepare_data("input.txt")
for instruction in instructions:
    paper = fold(paper, instruction)
print(uncode_paper(paper))
