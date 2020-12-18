# Advent of Code 2019
# Day 5: Sunny with a Chance of Asteroids
# https://adventofcode.com/2019/day/5

from itertools import permutations

acs_program = [3,8,1001,8,10,8,105,1,0,0,21,38,59,76,89,106,187,268,349,430,99999,3,9,1002,9,3,9,101,2,9,9,1002,9,4,9,4,9,99,3,9,1001,9,5,9,1002,9,5,9,1001,9,2,9,1002,9,3,9,4,9,99,3,9,1001,9,4,9,102,4,9,9,1001,9,3,9,4,9,99,3,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,1002,9,3,9,101,5,9,9,1002,9,3,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99]
# sample1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
# sample2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
# sample3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

def initialize(opcode):
    _id = int(opcode % 100)
    _mode1 = int((opcode / 100) % 10)
    _mode2 = int((opcode / 1000) % 10)
    _mode3 = 0
    if (_id == 3) or (_id == 4):
        _step = 2
    elif (_id == 5) or (_id == 6):
        _step = 3
    else:  # (_id == 1) or (_id == 2) or (_id ==7) or (_id ==8)
        _step = 4
    return _id, _mode1, _mode2, _mode3, _step

def define_param(p,i,opcode,step):
    params = []
    for x in range(1,int(step)):
        try:
            if opcode[x] == 1:
                params.append(p[i+x])
            elif opcode[x] == 0:
                params.append(p[p[i+x]])
        except IndexError:
            pass
    return params

def computer(program,phase_setting,last_output):
    p = program
    i = 0
    _inputcount = 0
    while i < len(p):
        opcode = initialize(p[i])
        step = opcode[4]
        params = define_param(p,i,opcode,step)

        if opcode[0] == 99:
            print("Program Finished")
            break
        elif opcode[0] == 1:
            p[p[i + 3]] = params[0] + params[1]
            i += step
        elif opcode[0] == 2:
            p[p[i + 3]] = params[0] * params[1]
            i += step
        elif opcode[0] == 3:
            if _inputcount == 0:
                p[p[i+1]] = int(phase_setting)
            else:
                p[p[i + 1]] = int(last_output)
            i += step
            _inputcount += 1
        elif opcode[0] == 4:
            return params[0]
        elif opcode[0] == 5:
            if params[0] != 0:
                i = params[1]
            else:
                i += step
        elif opcode[0] == 6:
            if params[0] == 0:
                i = params[1]
            else:
                i += step
        elif opcode[0] == 7:
            if params[0] < params[1]:
                p[p[i + 3]] = 1
            else:
                p[p[i + 3]] = 0
            i += step
        elif opcode[0] == 8:
            if params[0] == params[1]:
                p[p[i + 3]] = 1
            else:
                p[p[i + 3]] = 0
            i += step

def max_amp(software):
    combinations = permutations([0,1,2,3,4])
    thruster_signals = {}
    for combo in list(combinations):
        amp = 0
        last = 0
        for k in range(5):
            amp = computer(software,combo[k],last)
            last = amp
        thruster_signals[combo] = amp
    keymax = max(thruster_signals, key=thruster_signals.get)
    return keymax, thruster_signals[keymax]

max_signal = max_amp(acs_program)[1]

print(f"Highest Signal: {max_signal}")

# Ans:199988
