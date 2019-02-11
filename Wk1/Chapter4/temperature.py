#!/usr/bin/env python3

# Temperature module


# Accepts degrees fahrenheit, returns degrees celsius
def toCelsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


# Accepts degrees celsius, returns degrees fahrenheit
def toFahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit
