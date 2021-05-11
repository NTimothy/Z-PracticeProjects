# Advent of Code 2020
# --- Day 9: Encoding Error ---

def readFile():
    p_input = []
    count = 0
    try:
        f = open(r"day9", "r")
        line = f.readline()
        while line:
            p_input.append(int(line))
            line = f.readline()
            count +=1
    finally:
        f.close()
        return p_input, count

p_input, count = readFile()

def validateP1(_s,_num):
    for a in _s:
        for b in _s:
            c = a + b       # Summation
            if c == _num:
                return True
    return False


def validateP2(_s,_num):
    _sum = 0
    for x in _s:
        _sum += x
    if _sum == _num:
        return True
    return False


# Finds first invalid number
def firstInvalid(_pinput, preamble_length):
    _i = preamble_length                         # Defines starting index
    while _i < len(_pinput):
        preamble = _pinput[(_i - preamble_length):_i]  # Defines preamble slice
        v = validateP1(preamble, _pinput[_i])
        if v == False:
            return _pinput[_i], _i
        _i += 1


def findWeakness(_pinput,num):
    check = False
    _length = 0
    while _length <= len(_pinput):
        _shift = 0
        _end = 2 + _length
        while _end <= len(_pinput):                 # Defines set and validates
            _start = 0 + _shift
            s = []
            while _start < _end:
                s.append(_pinput[_start])
                _start += 1
            check = validateP2(s,_pinput[num])
            if check == True:
                _sum = min(s) + max(s)
                return s, _sum
            _shift +=1
            _end +=1
        _length +=1

# Using Test Inputs
# t_input = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]
# a, b = firstInvalid(t_input,5)
# s, sum = findWeakness(t_input,b)
# print("Test Input:")
# print(f"  Part 1: {a} \n  Part 2: {sum}")

# Using Puzzle Input
a, b = firstInvalid(p_input,25)
s, sum = findWeakness(p_input,b)
print("Puzzle Input")
print(f"  Part 1: {a} \n  Part 2: {sum}")


