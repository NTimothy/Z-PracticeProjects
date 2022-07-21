# Advent of Code 2020
# --- Day 10: Adapter Array ---

def readFile():
    p_input = []
    try:
        f = open(r"2020_day10", "r")
        line = f.readline()
        while line:
            p_input.append(int(line))
            line = f.readline()
    finally:
        f.close()
        return p_input

def findDifferences(list):
    a = 1
    _one = 0
    _three = 0
    while a < len(list):
        diff = list[a]-list[a-1]
        if diff == 1:
            _one += 1
        elif diff == 3:
            _three += 1
        a += 1
    product = _one * _three
    return product


p_input = readFile()
dev_rating = (max(p_input) + 3)      # Calculates device rating
p_input.extend([0, dev_rating])      # Accounts for outlet and device rating for puzzle input
p_input.sort()
print(f"Part 1: {findDifferences(p_input)}")
