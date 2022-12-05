
options = {
	"Rock" : ("A", 1),
	"Paper" : ("B", 2),
	"Scissors": ("C", 3)
}

scores = {
	"Win" : (6, "Z"),
	"Draw": (3, "Y"),
	"Lose": (0, "X")
}

data = [x.rstrip() for x in open("input.txt", "r").readlines()]

total_score = 0

for line in data:
	them, me = line.split()

	for key, value in options.items():
		if them in value[0]:
			their_choice = key

	for key, value in scores.items():
		if me in value[1]:
			my_need = key

	match their_choice:
		case "Rock":
			match my_need:
				case "Win":
					my_choice = "Paper"
				case "Lose":
					my_choice = "Scissors"
				case "Draw":
					my_choice = "Rock"

		case "Paper":
			match my_need:
				case "Win":
					my_choice = "Scissors"
				case "Lose":
					my_choice = "Rock"
				case "Draw":
					my_choice = "Paper"

		case "Scissors":
			match my_need:
				case "Win":
					my_choice = "Rock"
				case "Lose":
					my_choice = "Paper"
				case "Draw":
					my_choice = "Scissors"

	my_score = scores[my_need][0] + options[my_choice][1]
	total_score += my_score

print(total_score)

