#!/usr/bin/env python3

# Lecture 2 Python Introduction S105
# Function that uses local variables

def calcTax(amount, taxRate):
    tax = amount * taxRate      # tax is a local variable
    return tax                  # return is necessary


def main():
    tax = calcTax(85.0, .05)    # tax is a local variable
    print("Tax: " + str(tax))   # Tax 4.25


if __name__ == "__main__":
    main()
