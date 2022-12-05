
options = {
	"Rock" : (["A", "X"], 1),
	"Paper" : (["B", "Y"], 2),
	"Scissors": (["C", "Z"], 3)
}

scores = {
	"Win" : 6,
	"Draw": 3,
	"Lose": 0
}

data = [x.rstrip() for x in open("input.txt", "r").readlines()]

total_score = 0

for line in data:
	them, me = line.split()

	for key, value in options.items():
		if them in value[0]:
			their_choice = key

		if me in value[0]:
			my_choice = key

	match their_choice:
		case "Rock":
			match my_choice:
				case "Rock":
					my_result = "Draw"
					their_result = "Draw"
				case "Paper":
					my_result = "Win"
					their_result = "Lose"
				case "Scissors":
					my_result = "Lose"
					their_result = "Win"

		case "Paper":
			match my_choice:
				case "Rock":
					my_result = "Lose"
					their_result = "Win"
				case "Paper":
					my_result = "Draw"
					their_result = "Draw"
				case "Scissors":
					my_result = "Win"
					their_result = "Lose"

		case "Scissors":
			match my_choice:
				case "Rock":
					my_result = "Win"
					their_result = "Lose"
				case "Paper":
					my_result = "Lose"
					their_result = "Win"
				case "Scissors":
					my_result = "Draw"
					their_result = "Draw"

	my_score = scores[my_result] + options[my_choice][1] 
	their_score = scores[their_result] + options[their_choice][1]

	total_score += my_score

print(total_score)

