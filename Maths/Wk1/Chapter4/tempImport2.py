#!/usr/bin/env python3

# importing into a specified namespace

import temperature as temp

c = temp.toCelsius(50)
f = temp.toFahrenheit(50)

print("50 fahrenheit to celsius: " + str(c))
print("50 celsiss to fahrenheit: " + str(f))
