#!/usr/bin/env python3

# Importing one function into the global namespace

from temperature import toCelsius

c = toCelsius(50)

print("50 fahrenheit to celsius: " + str(c))
