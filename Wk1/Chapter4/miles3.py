#!/usr/bin/env python3

# A function that accepts two arguments and returns a value


def calculate_miles_per_gallon(miles_driven, gallons):
    mpg = miles_driven / gallons
    mpg = round(mpg, 3)
    return mpg


miles = 500
gallons = 14
mpg = calculate_miles_per_gallon(miles, gallons)   #35.7
print("Miles per gallon: " + str(mpg))
