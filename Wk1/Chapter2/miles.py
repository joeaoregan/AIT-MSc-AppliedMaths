#!/usr/bin/env python3

# display a title
print("The Miles Per Gallon program")
print

# get input from the user
milesDriven = float(input("Enter miles driven:\t\t"))
gallonsUsed = float(input("Enter gallons of gas used:\t"))

# calculate and round miles per gallon
mpg = milesDriven / gallonsUsed
mpg = round(mpg, 2)

# display the result
print
print("Miles Per Gallon:\t\t" + str(mpg))
print
print("Bye")
