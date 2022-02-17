def readFile():
    try:
        f = open(r"01.txt", "r")
        line = f.readline()
        p_input = []
        count = 0
        while line:
            p_input.append(int(line))
            line = f.readline()
            count +=1
    finally:
        f.close()
        return p_input, count

def part1(a):
    i = 0
    inc = 0
    while i < (len(a)-1):
        i+=1
        delta = (a[i] - a[i-1])
        if delta>0:
            inc += 1
    print(f"Increased {inc} times.")


def part2(a):
    i = 0
    inc = 0
    while i < (len(a)-4):
        i+=1
        window_a = (a[i] + a[i + 1] + a[i + 2])
        window_b = (a[i+1] + a[i + 2] + a[i + 3])
        delta = window_b-window_a
        if delta>0:
            inc += 1
    print(f"Window increased {inc} times.")

a,b = readFile()
part1(a)
part2(a)
""" 
Summary
Part 1  Determining positive delta values
Part 2  Determining positive moving sum with n = 3
"""
