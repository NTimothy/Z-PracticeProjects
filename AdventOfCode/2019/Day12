# Advent of Code 2019
# Day 12: The N-Body Problem
# https://adventofcode.com/2019/day/12
# <x=5, y=4, z=4>
# <x=-11, y=-11, z=-3>
# <x=0, y=7, z=0>
# <x=-13, y=2, z=10

import numpy as np

input = [5, 4, 4, -11, -11, -3, 0, 7, 0, -13, 2, 10]
p = np.asarray(input).reshape(4,3)
v = np.full(12,0).reshape(4,3)

total = 0       # zero starting energy
time = 0

for time in range(1000):
    for j in range(3):
        for i in range(4):
            try:
                for k in range(1,4):
                    if p[i][j] > p[i+k][j]:
                        v[i][j] -= 1
                        v[i+k][j] += 1
                    elif p[i][j] < p[i+k][j]:
                        v[i][j] += 1
                        v[i+k][j] -= 1
            except IndexError:
                pass
    for j in range(3):
        for i in range(4):
            p[i][j] += v[i][j]
    time +=1

for _i in range(4):
    _pe = 0
    _ke = 0
    for _j in range(3):
        _pe += abs(p[_i][_j])
        _ke += abs(v[_i][_j])
    total += (_pe*_ke)

print(f"\n@ Step #{time}")
print(f"Positions:\n", p)
print(f"Velocities:\n", v)
print(f"Total Energy: ", total)
