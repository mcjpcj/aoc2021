class HydroThermalVent:
    def __init__(self, data):
        self.beg = (
            int(data.split()[0].split(",")[0]),
            int(data.split()[0].split(",")[1]),
        )
        self.end = (
            int(data.split()[2].split(",")[0]),
            int(data.split()[2].split(",")[1]),
        )
        if self.beg[0] == self.end[0]:
            self.points = [
                (self.beg[0], y)
                for y in range(
                    min(self.beg[1], self.end[1]), max(self.beg[1], self.end[1]) + 1
                )
            ]
            self.diag = False
        elif self.beg[1] == self.end[1]:
            self.points = [
                (x, self.beg[1])
                for x in range(
                    min(self.beg[0], self.end[0]), max(self.beg[0], self.end[0]) + 1
                )
            ]
            self.diag = False
        else:
            x_factor = 1
            y_factor = 1
            if self.beg[0] > self.end[0]:
                x_step = -1
            if self.beg[1] > self.end[1]:
                y_step = -1
            xs = list(range(self.beg[0], self.end[0] + 1 * x_step, x_step))
            ys = list(range(self.beg[1], self.end[1] + 1 * y_step, y_step))
            self.points = [(x, y) for x, y in zip(xs, ys)]
            self.diag = True


with open("input.txt", "r") as file:
    vents = [HydroThermalVent(line) for line in file.read().splitlines()]

# Part one
points_count = {}
for vent in vents:
    if not vent.diag:
        for point in vent.points:
            try:
                points_count[point] += 1
            except KeyError:
                points_count[point] = 1
print(len([i for i in points_count.values() if i >= 2]))

# Part two
points_count = {}
for vent in vents:
    for point in vent.points:
        try:
            points_count[point] += 1
        except KeyError:
            points_count[point] = 1
print(len([i for i in points_count.values() if i >= 2]))
