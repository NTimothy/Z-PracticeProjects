# Advent of Code 2019
# Day 2: 1202 Program Alarm
# https://adventofcode.com/2019/day/2

# Opcode 1 adds together values at new index from value of n+1 and n+2 and stores in n+3 position
# Opcode 2 same as 1 except product
# Opcode 99 indicates program should halt


p_input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,
          19,6,23,1,23,6,27,1,13,27,31,2,13,31,35,1,5,
          35,39,2,39,13,43,1,10,43,47,2,13,47,51,1,6,51,
          55,2,55,13,59,1,59,10,63,1,63,10,67,2,10,67,71,
          1,6,71,75,1,10,75,79,1,79,9,83,2,83,6,87,2,87,9,
          91,1,5,91,95,1,6,95,99,1,99,9,103,2,10,103,107,1,
          107,6,111,2,9,111,115,1,5,115,119,1,10,119,123,1,2,
          123,127,1,127,6,0,99,2,14,0,0]

print("Unmodified Input:", p_input)


def findpos(i):
    a = p_input[i + 1]
    b = p_input[i + 2]
    c = p_input[i + 3]
    x = p_input[a]
    y = p_input[b]
    return x,y,c

i=0
p_input[1] = 12
p_input[2] = 2
print("Modified:",p_input)
while True:
    try:
        if p_input[i] == 99:
            print("Final:", p_input)
            print("\nPart 1 Solution :", p_input[0])
            break

        elif p_input[i] == 1:
            x,y,c = findpos(i)
            sum = x + y
            p_input[c] = sum
            continue

        elif p_input[i] == 2:
            x,y,c = findpos(i)
            product = x * y
            p_input[c] = product
            continue
    finally:
        i += 4

# Part 1 Solution p_input[0] == 12490719


print("\n-----PART 2-----\n")

# Part 2 wants to determine 'noun' and 'verb' inputs that
# give output at opcode[0] == 19690720
# and to solve for 100 * noun + verb
# Part 2 solution: 2003


p_input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,
          19,6,23,1,23,6,27,1,13,27,31,2,13,31,35,1,5,
          35,39,2,39,13,43,1,10,43,47,2,13,47,51,1,6,51,
          55,2,55,13,59,1,59,10,63,1,63,10,67,2,10,67,71,
          1,6,71,75,1,10,75,79,1,79,9,83,2,83,6,87,2,87,9,
          91,1,5,91,95,1,6,95,99,1,99,9,103,2,10,103,107,1,
          107,6,111,2,9,111,115,1,5,115,119,1,10,119,123,1,2,
          123,127,1,127,6,0,99,2,14,0,0]

p_input[1] = 12
p_input[2] = 2

def intcode_program(p_input):
    z = p_input[:]

    for i in range(0, len(z), 4):
        operator = z[i]
        x = z[z[i + 1]]
        y = z[z[i + 2]]
        if operator == 99:
            return z[0]
        elif operator == 1:
            z[z[i + 3]] = x + y
        elif operator == 2:
            z[z[i + 3]] = x * y
    return z[0]

for n in range(100):
    for v in range(100):
        p_input[1] = n
        p_input[2] = v

        ans = intcode_program(p_input)
        if ans == 19690720:
            print("Part 2 Solution:", 100 * n + v)
            break

