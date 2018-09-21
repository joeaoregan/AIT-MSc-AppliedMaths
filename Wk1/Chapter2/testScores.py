#!/usr/bin/env python3

# S28 Python Introduction

# This is a tutorial program that illustrates the use of
# the while and if statements

# initialise variables
counter = 0
scoreTotal = 0
testScore = 0

# get scores
while testScore != 999:
    testScore = int(input("Enter test score: "))
    if testScore >= 0 and testScore <= 100:
        scoreTotal += testScore   # add score to total
        counter += 1                # add 1 to counter

# calculate average score
#average_score = score_total / counter
#average_score = round(average_score)
average_score = round(      # implicit continuation
    scoreTotal / counter)  # same results as
                            # commented out statements
# display the result
print ("========================")
print("Total Score: " + str(scoreTotal)  # implicit continuation
      + "\nAverage Score: " + str(average_score))
