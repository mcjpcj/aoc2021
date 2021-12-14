class Cave:
    def __init__(self, id):
        self.id = id
        self.connected = []
        if id.isupper():
            self.type = "BIG"
        else:
            self.type = "SMALL"

    def add_connection(self, con):
        self.connected.append(con)


class CavePath:
    def __init__(self, map=["start"]):
        self.map = map

    def check_if_can_go(self, new_cave):
        if new_cave in self.map and new_cave.type != "BIG":
            return False
        else:
            return True

    def check_if_visited_small_cave_twice(self):
        small_caves = [cave for cave in self.map if cave.islower()]
        return len(small_caves) == len(set(small_caves))

    def possible_caves_part_one(self):
        return [
            cave
            for cave in caves[self.map[-1]].connected
            if cave not in self.map or caves[cave].type == "BIG"
        ]

    def possible_caves_part_two(self):
        if self.check_if_visited_small_cave_twice():
            return [
                cave
                for cave in caves[self.map[-1]].connected
                if cave != "start"
                and self.map.count(cave) < 2
                or caves[cave].type == "BIG"
            ]
        else:
            return self.possible_caves_part_one()


with open("input.txt", "r") as file:
    data = file.read().splitlines()
caves = {}
for line in data:
    beg, end = line.split("-")
    try:
        caves[beg].add_connection(end)
    except KeyError:
        caves[beg] = Cave(beg)
        caves[beg].add_connection(end)

    try:
        caves[end].add_connection(beg)
    except KeyError:
        caves[end] = Cave(end)
        caves[end].add_connection(beg)

# Part one
paths = [CavePath()]
finished = []
i = 0
while paths != []:
    path = paths.pop()
    for cave in path.possible_caves_part_one():
        map = path.map.copy() + [cave]
        if cave == "end":
            finished.append(map)
        else:
            paths.append(CavePath(map))
print(len(finished))
# Part two
paths = [CavePath()]
finished = []
i = 0
while paths != []:
    path = paths.pop()
    for cave in path.possible_caves_part_two():
        map = path.map.copy() + [cave]
        if cave == "end":
            finished.append(map)
        else:
            paths.append(CavePath(map))
print(len(finished))
