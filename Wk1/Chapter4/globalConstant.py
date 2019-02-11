#!/usr/bin/env python3

TAX_RATE = 0.05                 # TAX_RATE is global


def calcTax(amount):
    tax = amount * TAX_RATE     # use constant
    return tax


taxAmount = calcTax(100)
print("Tax Amount: " + str(taxAmount))
