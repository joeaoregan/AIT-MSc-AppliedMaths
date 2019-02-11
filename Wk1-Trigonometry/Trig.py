'''
Joe O'Regan
A00258304
Wk1-Trigonometry Assignment
Part 1: Trig 2
'''

import math as m


def trigFunction(angle, distance):
    height = distance * (m.tan(m.radians(angle)))
    return height


def main():
    d = float(input("Enter the distance to object: "))
    a = float(input('Enter Angle of Elevation: '))
    h = trigFunction(a, d)
    #print('Height of object is: %s' %format(float(h), '0.2E'))
    print('Height of object is: %.2f' %h)


if __name__ == "__main__":
    main()
