# Advent of Code 2020
# --- Day 12: Rain Risk ---

import math

def readFile():
    p_input = []
    try:
        f = open(r"2020_day12", "r")
        line = f.readline()
        while line:
            l = line.strip()
            p_input.append(l)
            line = f.readline()
    finally:
        f.close()
        return p_input


f = readFile()


def find_distance1(data):
    length = len(data)
    i = 0
    cardinal = ["N", "E", "S", "W", "F"]
    _angle = 0                          # Assuming "East" facing start direction
    x, y = 0,0                          # Assuming (0,0) start coordinates
    while i < length:
        a, b = data[i][0], data[i][1:]
        if a in cardinal:
            _x, _y = move_ship1(a, int(b), _angle)
            x += _x
            y += _y
        else:
            turn = change_direction1(a)
            _angle += (int(turn) * int(b))

        while abs(_angle) >= 360:
            if _angle >= 360:
                _angle -= 360
            elif _angle <= -360:
                _angle += 360
        # print(f"Instruction:{a}{b} | Change: ({x},{y},{_angle})")   # Debug: Prints ship status after each instruction
        i += 1
    _total = abs(x) + abs(y)

    print(f"Part 1: Manhattan distance: {_total} ")


def move_ship1(_direction,_distance,_angle):
    _x, _y = 0, 0
    if _direction == "F":
        _y = round(math.sin(math.radians(_angle)) * _distance)
        _x = round(math.cos(math.radians(_angle)) * _distance)
    elif _direction == "N":
        _y += _distance
    elif _direction == "E":
        _x += _distance
    elif _direction == "S":
        _y -= _distance
    elif _direction == "W":
        _x -= _distance
    return _x, _y


def change_direction1(_dir):
    if _dir == "L":
        return 1
    elif _dir == "R":
        return -1

find_distance1(f)    # Part 1



