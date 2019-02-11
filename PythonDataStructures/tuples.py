#!/usr/bin/env python3

# Tuples: Can'y change values

months=('January','February','March','April','May','June','July','August','September','October','November','December')
print("The months of the year include:")
for month in months:
    print(month)

print("The last 6 months of the year are {0}" .format(months[6:]))

aTuple=12345,"Karol","Peter",True,3.99
print(aTuple)
anotherTuple =aTuple,(5,6,7,8),'Harry'
print(anotherTuple)
print('===============================================')