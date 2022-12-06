
import pandas as pd
import numpy as np

print(" ")
print("Part 1:")
print(" ")

df = pd.read_csv("input.txt", sep = " ", header = None)
shape = np.full(len(df), np.nan) # create new collumn, NaN, to be filled
df[2] = shape
#print(df)
print("length of imported df: ",len(df[0]))

# turn data frame collumns into callable lists
opp = df[0].to_numpy()
you = df[1].to_numpy()
score = df[2].to_numpy()

#print("opp: ", opp)
#print("you: ", you)
#print("score: ", score)

for row in range(len(opp)):
    # You play Rock
    if you[row] == "X":
        score[row] = 1 # assigned score for playing Rock

        if opp[row] == "A": # opponent plays Rock: draw
            score[row] +=3
        if opp[row] =="C": # opponent plays Scissors: you win
            score[row] +=6

    # You play Paper
    if you[row] == "Y":
        score[row] = 2 # assigned score for playing paper

        if opp[row] == "B": # oppponent plays paper: draw
            score[row] +=3
        if opp[row] == "A": # opponent plays Rock: you win
            score[row] +=6

    # you play Scissors    
    if you[row] == "Z":
        score[row] = 3 # assigned score for playing scissors

        if opp[row] == "C": # opponent plays scissors: draw
            score[row] +=3
        if opp[row] == "B": # opponent plays paper: you win
            score[row] +=6


#print(df)
print("length of new df: ",len(df[2]))
print("total score = ", df[2].sum())


"""
the second column says how the round needs to end:
X means you need to lose,
Y means you need to end the round in a draw,
Z means you need to win.

The total score is still calculated in the same way,
but now you need to figure out what shape to choose so the round ends as indicated.
"""

print(" ")
print("Part 2:")
print(" ")

#opp is opponent shape from before
outcome = df[1].to_numpy() # should you win or lose
score_2 = [0]*len(df) #np.full(len(df), np.nan)

#print("opponent plays: ", opp)
#print("Desired outcome: ", outcome)
#print("score after each round: ", score_2)

for i in range(len(opp)):
    # opponent plays Rock
    if opp[i] == "A":
        if outcome[i] == "X": # Desired outcome: Loose. Play Scissors
            score_2[i] += 3 # 3 + 0
        if outcome[i] == "Y": # Desired outcome: Draw, so play Rock
            score_2[i] += 4 # 1 + 3
        if outcome[i] == "Z": # Desired: Win. Pay: paper
            score_2[i] += 8 # 2 + 6
    
    # Opponent plays Paper
    if opp[i] == "B":
        if outcome[i] == "X": # Desired outcome: Loose. Play Rock
            score_2[i] += 1 # 1 + 0
        if outcome[i] == "Y": # Desired outcome: Draw, so play Paper
            score_2[i] += 5 # 2 + 3
        if outcome[i] == "Z": # Desired: Win. Pay: Scissors
            score_2[i] += 9 # 3 + 6

    # Opponent plays Scissors
    if opp[i] == "C":
        if outcome[i] == "X": # Desired outcome: Loose. Play Paper
            score_2[i] += 2 # 2 + 0
        if outcome[i] == "Y": # Desired outcome: Draw, so play Scissors
            score_2[i] += 6 # 3 + 3
        if outcome[i] == "Z": # Desired: Win. Pay: Rock
            score_2[i] += 7 # 1 + 6


#print("score after each round: ", score_2)
print("total score: ", sum(score_2))