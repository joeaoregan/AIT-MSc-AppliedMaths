#!/usr/bin/env python 3

# A break statement that exits and infinite while loop

print("Enter 'exit' when you're done.\n")
while True:
    data = input("Enter an integer to square: ")
    if data == "exit":
        break
    i = int(data)
    print(i, " squared is ", i * i, "\n")
print("Okay, bye!")
