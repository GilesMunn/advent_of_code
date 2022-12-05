

data = open("input.txt", "r").readlines()

elves = []
current = []
sums = []

for line in data:
	line = line.rstrip()
	if line != "":
		current.append(int(line))
	else:
		elves.append(current)
		current = []
elves.append(current)

for elf in elves:
	sums.append(sum(elf))

print(sorted(sums))
print()
print(sorted(sums)[-3:])
print(sum(sorted(sums)[-3:]))