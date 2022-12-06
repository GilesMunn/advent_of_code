"""
https://adventofcode.com/2022/day/3
"""


import string as s
import numpy as np


with open("input.txt") as f:
    lines = f.readlines()


def weight(string):
    lower_letters = list(s.ascii_lowercase)
    upper_letters = list(s.ascii_uppercase)
    letters = lower_letters + upper_letters
    dict = {}
    priority  = np.linspace(1, 52, 52) # start, stop, number of values
    #print("priority: ", priority)

    for i in range(len(letters)):
        if len(letters) == len(priority):
            dict[letters[i]] = priority[i]
        else:
            print("Error in priority assignment")
    
    return dict[string[0]]
    
#print("weight function output weight if r: ", weight("r"))

print("Task 1:")

count = 0 

for x in lines:
    length = len(x)
    split = int((length+1)/2) - 1

    comp1 = x[:split]
    comp2 = x[split:]

    overlap = list(set(comp1).intersection(comp2))

    count += weight(overlap)

    #print(comp1)
    #print(comp2)
    #print(overlap)
    #print(count)


print("sum of all overlaps:", count)
print(" ")

"""
Task two: overlap in lines of three, sum of those weights.
https://adventofcode.com/2022/day/3#part2
"""
print("Task 2:")

count_2 = 0

for j in range(0, len(lines), 3):
    chunk = lines[j:j+3]
    #print(chunk)
    overlap = list(set(chunk[0]).intersection(chunk[1]))
    overlap = list(set(overlap).intersection(chunk[2]))
    if "\n" in overlap:
        overlap.remove("\n")
    
    count_2 += weight(overlap)
    
    #print(overlap)
    #print(count_2)


print("weight of three-way overlaps: ", count_2)



