with open("input.txt", "r") as file:
    data = file.read().splitlines()

# Part one
close_to_open = {")": "(", "]": "[", "}": "{", ">": "<"}
open_to_close = {val: key for key, val in close_to_open.items()}
close_to_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
close_to_score = {")": 1, "]": 2, "}": 3, ">": 4}
points = []


def get_first_illegal_char(line):
    opened = []
    for char in line:
        if char in "([{<":
            opened.append(char)
        elif close_to_open[char] != opened.pop():
            return char


for line in data:
    illegal_char = get_first_illegal_char(line)
    if illegal_char:
        points.append(close_to_points[illegal_char])
print(sum(points))
# Part two
def get_chunk_end(line):
    opened = []
    for char in line:
        if char in "([{<":
            opened.append(char)
        else:
            open_char_idx = len(opened) - opened[::-1].index(close_to_open[char]) - 1
            opened.pop(open_char_idx)
    return [open_to_close[char] for char in opened[::-1]]


def calc_score(chunk_end):
    score = 0
    for char in chunk_end:
        score = 5 * score + close_to_score[char]
    return score


scores = []
for line in data:
    if not get_first_illegal_char(line):
        chunk_end = get_chunk_end(line)
        score = calc_score(chunk_end)
        scores.append(score)
print(sorted(scores)[len(scores) // 2])
