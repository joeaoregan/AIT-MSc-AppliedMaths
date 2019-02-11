#!/usr/bin/env python3

def calculateFutureValue(monthlyInvestment, yearlyInterest, years):
    # convert yearly values to monthly values
    monthlyInterestRate = yearlyInterest / 12 / 100.0
    months = years * 12

    print("Monthly Interest Rate: " + str(monthlyInterestRate))
    print("Months: " + str(months))

    # calculate future value
    futureValue = 0.0
    for i in range(1, months):
        futureValue += monthlyInvestment

        monthlyInterest = futureValue * monthlyInterestRate

        futureValue += monthlyInterest
        print("i = " + str(i) + " future value = " + str(futureValue))

    return round(futureValue, 2)


def main():
    monthlyInvestment = 0

    while monthlyInvestment <= 0 or monthlyInvestment > 1000:
        #print("Enter monthly investment:\t")
        #monthlyInvestment = input()
        #monthlyInvestment = input("Enter monthly investment:\t")
        monthlyInvestment = int(input("Enter monthly investment:\t"))   # need to cast input to integer

        if monthlyInvestment <= 0 or monthlyInvestment > 1000:
            print("Entry must be greater than 0 and less than or equal to 1000")

    # print("Enter yearly interest rate:\t")
    yearlyInterest = int(input("Enter yearly interest rate:\t"))
    # yearlyInterest = get_float("Enter Number: ", 0, 10)
    numYears = int(input("Enter number of years:\t\t"))

    #f utureAmount = calculateFutureValue(100,.05,5)
    futureAmount = calculateFutureValue(monthlyInvestment,yearlyInterest,numYears)
    print("Future value:\t\t\t\t" + str(futureAmount))


if __name__ == "__main__":
    main()
