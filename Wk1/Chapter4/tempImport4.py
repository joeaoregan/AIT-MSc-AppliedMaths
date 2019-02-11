#!/usr/bin/env python3

# Importing all functions into the global namespace

from temperature import *

c = toCelsius(50)
f = toFahrenheit(50)

print("50 fahrenheit to celsius: " + str(c))
print("50 celsius to fahrenheit: " + str(f))
