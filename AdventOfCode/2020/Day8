# Advent of Code 2020
# Day 8

commands = {}

with open(r"2020_day8") as file:
    line = file.readline()
    x = 0
    while line:
        # action = str(line[0:3])
        # value = int(line[4:])
        commands[x] = line[0:-1].strip()
        line = file.readline()
        x += 1

def part1(_cmd):
    pos = 0
    acc = 0
    history = {}
    while pos < len(_cmd):
        key = _cmd[pos][0:3]
        value = int(_cmd[pos][4:])
        if pos in history.keys():
            print("Part 1 : {}".format(acc))    # Prints accumulator at loop start
            break
        else:
            history[pos] = value                # Position to history
        if key == "acc":
            acc += value
            pos += 1
            continue
        elif key == "jmp":
            pos += value
        elif key == "nop":
            pos +=1
            pass

part1(commands)
