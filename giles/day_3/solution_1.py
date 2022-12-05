import string

data = [x.rstrip() for x in open("input.txt", "r").readlines()]
priorities = string.printable[10:62]
total_sum = 0

for number, rucksack in enumerate(data, start=1):
	half = int(len(rucksack)/2)
	cmpt_1, cmpt_2 = rucksack[:half], rucksack[half:]
	in_common = {}

	for item in cmpt_1:
		if item in cmpt_2 and item not in in_common.keys():
			in_common[item] = priorities.index(item) + 1

	total_sum += sum(in_common.values())

print(f"Total sum: {total_sum}")

