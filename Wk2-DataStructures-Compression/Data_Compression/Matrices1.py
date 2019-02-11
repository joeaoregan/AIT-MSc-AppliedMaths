# 2. Data Structures % Data Compression
# Week 2 Data Compression - S16

import numpy as np
import math

N = 8
n = 8.0
T = np.zeros((N, N), dtype='float_')
Tt = np.zeros((N, N), dtype='float_')


def printMatrix(npArray):
    for r in range(N):
        print(" ")
        for c in range(N):
            print("{0:0.3f}".format(npArray[r][c]), end=' ')


def Generate_T():
    for r in range(N):
        for c in range(N):
            if(r==0):
                T[r][c] = 1/math.sqrt(n)
            else:
                T[r][c] = math.sqrt((2.0/n))* math.cos((r*math.pi*(2 * c + 1)) / (2*n))


def main():
    print("This script calculates the matrices T and T' as employed in DCT's")
    Generate_T()
    print("Matrix T")
    printMatrix(T)


if __name__=="__main__":
    main()
