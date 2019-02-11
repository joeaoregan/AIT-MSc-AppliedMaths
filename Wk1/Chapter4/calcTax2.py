#!/usr/bin/env python3

# Lecture 2 Python Introduction S106
# Function that changes a global variable (not recommended)

tax = 0.0                       # tax is global variable


def calcTax(amount, taxRate):
    global tax                  # access global variable
    tax = amount * taxRate      # change global variable


def main():
    calcTax(85.0, .05)
    print("Tax: " + str(tax))   # Tax 4.25 (global)


if __name__ == "__main__":
    main()
