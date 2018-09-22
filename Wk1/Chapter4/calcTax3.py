#!/usr/bin/env python3

# Lecture 2 Python Introduction S106
# A local variable that shadows a global variable (not recommended)

tax = 0.0                       # tax is global variable


def calcTax(amount, taxRate):
    tax = amount * taxRate      # tax is local variable
    print("Tax: " + str(tax))   # Tax 4.25 (local)


def main():
    calcTax(85.0, .05)
    print("Tax: " + str(tax))   # Tax 0.0 (global)


if __name__ == "__main__":
    main()
