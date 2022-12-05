import string

data = [x.rstrip() for x in open("input.txt", "r").readlines()]
priorities = string.printable[10:62]
total_sum = 0
group_no = 1
group = []

for rucksack in data:
	group.append(rucksack)

	if group_no % 3 == 0:

		badge, *_ = list(
			set(group[0]).intersection(group[1], group[2]))
		group = []
		total_sum += priorities.index(badge) + 1

	group_no += 1

print(f"Total sum: {total_sum}")

