import string
from collections import Counter


# Adds all possible lower case letters to a list as possible "questions"
letters = list(string.ascii_lowercase)
letters.extend([i+b for i in letters for b in letters])


def get_answers():
    answers = {}
    with open(r"2020_day6") as file:
        line = file.readline()
        num = 0
        new_group = True
        yes = 0
        while line:
            if new_group:
                answers[num] = []
                new_group = False
            if line != "\n":
                for c in line:
                    if (c in letters) and (c not in answers[num]):
                        answers[num].append(c)
                        yes += 1
                line = file.readline()
            elif line == "\n":
                num += 1
                new_group = True
                line = file.readline()
    return yes


x = get_answers()
print("Part 1 Sum:", x)             # Part 1 Ans: 6662

# Part 2

def get_similar_answers():
    answers = {}
    with open(r"2020_day6") as file:
        line = file.readline()
        yes = 0
        _group_ans = {}
        _people = 0
        while line:
            if line != "\n":                # if line contains answers
                _people += 1
                line = line.strip()
                for char in line:
                    if char not in _group_ans.keys():
                        _group_ans[char] = 1
                    elif char in _group_ans.keys():
                        _group_ans[char] += 1
                line = file.readline()
            elif line == "\n":                                  # Triggers when end of group is reached
                c = Counter(_group_ans.values())                # Counts frequency of questions
                _similar = max(Counter(_group_ans.values()))    # Finds highest frequency of questions
                if _similar == _people:                         # Checks if entire group answered "yes"
                    yes += c[_similar]                          # Adds to total
                _group_ans = {}                                 # Resets dict for next group
                _people = 0
                line = file.readline()                          # Continues to next line
    return yes

x = get_similar_answers()
print("Part 2 Sum:", x)
