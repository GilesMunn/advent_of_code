"""
day 1: A list of calories of snacks for each elf is povided.
Each elf leaves a line between to last.
Whic elf has the most calories, amd how manny calories?

SUCCESS
"""

with open("input.txt") as f:
    lines = f.readlines()

#print("lines = ", lines)
print(" ")

a = []

for x in lines:
    if x == "\n":
        x = 0
    #print(int(x))
    #print(" ")
    a.append(int(x))

#print("original a = ", a)
#print(" ")


# Produce a dictionary of what snacks each elf has

elf_dictionary = {}
num_elves = a.count(0)

while 0 in a:
    for number in range(num_elves):
        index_pos = a.index(0) # index of first 0 in list
        elf_dictionary["elf%s" %number] = a[:index_pos]
        del a[:index_pos+1]
        #print("elf1 = ", elf1)
        #print("updated a = ", a)
        #print(elf_dictionary)
        #print(" ")

else: elf_dictionary["elf"+str(num_elves)] = a
#print("elf_dictionary", elf_dictionary)
#print(" ")

# Dictionary of totsal calories each elf carries:

elf_sum = elf_dictionary

for key in elf_sum:
    elf_sum[key] = sum(elf_sum[key])

#print("elf_sum = ", elf_sum)

# Which elf carries the most:

top_elf = max(elf_sum, key=elf_sum.get)
print(top_elf, " has the most calories, with ", elf_sum[top_elf], " calories.")
print(" ")


"""
Part 2:
the Elves would instead like to know the total Calories carried by the top three Elves carrying
the most Calories
"""

# Define new dictionary, to remove top elf from and repeat
elf_sum_adjusted = elf_sum.copy() # need to do this to copy the dictionary, or all changes made will apply to both.

del elf_sum_adjusted[top_elf]
second_top_elf = max(elf_sum_adjusted, key=elf_sum_adjusted.get)

del elf_sum_adjusted[second_top_elf]
third_top_elf = max(elf_sum_adjusted, key=elf_sum_adjusted.get)

print("the top three elves are: ", top_elf, second_top_elf, third_top_elf)
print("their calories are: ", elf_sum[top_elf], elf_sum[second_top_elf], elf_sum[third_top_elf])
print("The total combined is: ", (elf_sum[top_elf] + elf_sum[second_top_elf] + elf_sum[third_top_elf]))
print(" ")