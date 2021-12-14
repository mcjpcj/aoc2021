def prepare_data(file_name):
    with open(file_name, "r") as file:
        start_template, insertion_rules = file.read().split("\n\n")
        insertion_rules = {
            rule.split(" -> ")[0]: rule.split(" -> ")[1]
            for rule in insertion_rules.splitlines()
        }
        return start_template, insertion_rules


def polymer_insert_part_one(template, rules):
    pairs = [template[i : i + 2] for i in range(len(template) - 1)]
    return template[0] + "".join([rules[pair] + pair[1] for pair in pairs])


def polymer_insert_part_two(pairs):
    new_pairs = {pair: 0 for pair in insertion_rules.keys()}
    element_count = {element: 0 for element in set(insertion_rules.values())}
    element_count[template[0]]
    for pair, count in pairs.items():
        if count > 0:
            pair1, pair2 = insertions[pair]
            new_pairs[pair1] += count
            new_pairs[pair2] += count
            element_count[pair2[0]] += count
            element_count[pair2[1]] += count
    return new_pairs, element_count


# Part one:
template, insertion_rules = prepare_data("input.txt")
for _ in range(10):
    template = polymer_insert_part_one(template, insertion_rules)
element_count = {element: template.count(element) for element in set(template)}
print(max(element_count.values()) - min(element_count.values()))

# Part two:
template, insertion_rules = prepare_data("input.txt")
beg_pairs = [template[i : i + 2] for i in range(len(template) - 1)]
insertions = {
    rule: [rule[0] + insertion_rules[rule], insertion_rules[rule] + rule[1]]
    for rule in insertion_rules.keys()
}
pairs = {pair: beg_pairs.count(pair) for pair in insertion_rules.keys()}
for _ in range(40):
    pairs, element_count = polymer_insert_part_two(pairs)
print(max(element_count.values()) - min(element_count.values()))
