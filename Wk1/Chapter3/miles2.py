#!/usr/bin/env python3

# Lecture 2 S94
# A continue statement that jumps to the beginning of a while loop

more = "y"
while more.lower() == "y":
    milesDriven = float(input("Enter miles driven:\t\t"))
    gallonsUsed = float(input("Enter gallons of gas used:\t"))

    # validate input
    if milesDriven <= 0 or gallonsUsed <= 0:
        print("Both entries must be greater than zero. "
              + "Try again.\n")
        continue

    mpg = round(milesDriven / gallonsUsed, 2)
    print("Miles Per Gallon:", mpg, "\n")

    more = raw_input("Continue? (y/n): ")
    print

print("Okay, bye!")
