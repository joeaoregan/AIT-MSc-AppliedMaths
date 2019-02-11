#!/usr/bin/env python3

# display a title
print("The Test Scores program")
print
print("Enter 3 test scores")
print("======================")

# get scores from the user and accumulate the total
totalScore = 0  # initialise the totalScore variable
totalScore += int(input("Enter test score: "))
totalScore += int(input("Enter test score: "))
totalScore += int(input("Enter test score: "))

# calculate average score
averageScore = round(totalScore / 3)

# format and display the result
print("======================")
#print("Total Score:  ",totalScore,
#      "\nAverage Score:", averageScore)
print("Total Score:  " + str(totalScore) +
      "\nAverage Score:" + str(averageScore))
print
print("Bye")
