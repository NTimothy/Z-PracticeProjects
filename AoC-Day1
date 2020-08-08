# Advent of Code 2019
# Day 1: The Tyranny of the Rocket Equation

"""
https://adventofcode.com/2019/day/1
"""
import math

def calc(m):
    fuel = math.floor(m/3) - 2  # equation given by examples
    return fuel

def test():
    ex1 = math.floor(12 / 3) - 2        # Output: 2
    ex2 = math.floor(14 / 3) - 2        # Output: 2
    ex3 = math.floor(1969 / 3) - 2      # Output: 2654
    ex4 = math.floor(100756 / 3) - 2    # Output: 33583
    print(ex1)
    print(ex2)
    print(ex3)
    print(ex4)


test()  # verify equation from examples given
print("\n")

f = open(r"C:\Users\ntimo\PycharmProjects\Testing\Z-PracticeProjects\day1", "r").readlines()
f_strip = []        # create empty lis to store input data

# strip list of newlines, convert to integer, append to new list
for element in f:
    f_strip.append(int(element.strip()))

print(f_strip)  # confirm list contains only integers
fuel = []       # empty list to contain module fuel values

for x in f_strip:
    y = calc(x)         # calculating fuel cost per module
    fuel.append(y)      # append to list containing individual module fuel requirements

print(sum(fuel))        # summation of module fuel costs

# Part 1 Solution: 3386686

# Part 2: Accounting for additional fuel required for fuel

f_1 = f_strip

total = 0
for x in f_1:
    y = calc(x)
    while True:
        if 0.5 < y:
            total += y
            y = calc(y)
            continue
        else:
            break

print("Estimated Fuel Costs:", total)
# Part 2 Solution: 5077155 
