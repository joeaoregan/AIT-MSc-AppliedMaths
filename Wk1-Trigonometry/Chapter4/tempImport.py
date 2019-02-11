#!/usr/bin/env python3

# importing into the module's default namespace

import temperature

c = temperature.toCelsius(50)
f = temperature.toFahrenheit(50)

print("50 fahrenheit to celsius: " + str(c))
print("50 celsius to fahrenheit: " + str(f))
