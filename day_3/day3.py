import re

filename = "data.txt"


def parse_input():
    with open(filename) as file:
        lines = file.readlines()
    return lines


def find_mul_indices(lines):
    pattern = r"mul\((\d+),\s*(\d+)\)"
    occurrences = []

    for line_number, line in enumerate(lines, start=1):
        for match in re.finditer(pattern, line):
            start_index = match.start()
            x, y = match.groups()
            occurrences.append({
                "line": line_number,
                "index": start_index,
                "values": int(x)*int(y)
            })
    return occurrences


def find_dont_indices(lines):
    pattern = r"don't\(\)"
    occurrences = []

    for line_number, line in enumerate(lines, start=1):
        for match in re.finditer(pattern, line):
            start_index = match.start()
            occurrences.append({
                "line": line_number,
                "index": start_index,
                "bool": False
            })
    return occurrences


def find_do_indices(lines):
    pattern = r"do\(\)"
    occurrences = []

    for line_number, line in enumerate(lines, start=1):
        for match in re.finditer(pattern, line):
            start_index = match.start()
            occurrences.append({
                "line": line_number,
                "index": start_index,
                "bool": True,
            })
    return occurrences

def activation_mul_range(do_occurrences, dont_occurrences, mul_ocurrences):
    all_occurrences = do_occurrences + dont_occurrences + mul_ocurrences
    sorted_occurrences = sorted(all_occurrences, key=lambda x: (x["line"], x["index"]))
    state = True
    res = 0
    for occurrence in sorted_occurrences:
        if state == True:
            if "bool" in occurrence:
                state = occurrence["bool"]
            if "values" in occurrence:
                res += occurrence["values"]
        if state == False:
            if "bool" in occurrence:
                state = occurrence["bool"]
    return res






lines = parse_input()
mul_occurrences = find_mul_indices(lines)
do_occurrences = find_do_indices(lines)
dont_occurrences = find_dont_indices(lines)
print(activation_mul_range(do_occurrences, dont_occurrences, mul_occurrences))


