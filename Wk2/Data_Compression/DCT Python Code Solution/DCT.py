import math
import numpy as np
from copy import copy, deepcopy


class DCT_Demo(object):
    def __init__(self, level):
        self.N = 8
        self.n = 8.0
        self.T = np.zeros((self.N, self.N), dtype='float_')
        self.Tt = np.zeros((self.N, self.N), dtype='float_')
        self.DCT = np.zeros((self.N, self.N), dtype='float_')
        self.TM = np.zeros((self.N, self.N), dtype='float_')
        self.R = np.zeros((self.N, self.N), dtype='float_')
        self.Q_Mat = np.zeros((self.N, self.N), dtype='int32')
        self.C = np.zeros((self.N, self.N), dtype='int32')
        self.fin = np.zeros((self.N, self.N), dtype='int32')

        self.Q50 = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                             [12, 12, 14, 19, 26, 58, 60, 55],
                             [14, 13, 16, 24, 40, 57, 69, 56],
                             [14, 17, 22, 29, 51, 87, 80, 62],
                             [18, 22, 37, 56, 68, 109, 103, 77],
                             [24, 35, 55, 64, 81, 104, 113, 92],
                             [49, 64, 78, 87, 103, 121, 120, 101],
                             [72, 92, 95, 98, 112, 100, 103, 99]])

        self.M = np.array([[16, 8, 23, 16, 5, 14, 7, 22],
                           [20, 14, 22, 7, 14, 22, 24, 6],
                           [15, 23, 24, 23, 9, 6, 6, 20],
                           [14, 8, 11, 14, 12, 12, 25, 10],
                           [10, 9, 11, 9, 13, 19, 5, 17],
                           [8, 22, 20, 15, 12, 8, 22, 17],
                           [24, 22, 17, 12, 18, 11, 23, 14],
                           [21, 25, 15, 16, 23, 14, 22, 22]])

        self.Qlevel = level
        self.Generate_T()
        self.CalculateQ()

    def Calculate_FDCT(self):
        sum = 0.0
        for r in range(self.N):
            for c in range(self.N):
                for k in range(self.N):
                    sum = (sum + self.T[r][k] * self.M[k][c])
                self.TM[r][c] = sum
                sum = 0.0
        sum = 0.0
        for r in range(self.N):
            for c in range(self.N):
                for k in range(self.N):
                    sum = (sum + self.TM[r][k] * self.Tt[k][c])
                self.DCT[r][c] = sum
                sum = 0.0
        np.matmul(self.T, self.M)

    def Calculate_IDCT(self):
        sum = 0.0
        for r in range(self.N):
            for c in range(self.N):
                for k in range(self.N):
                    sum = (sum + self.Tt[r][k] * self.R[k][c])
                self.TM[r][c] = sum
                sum = 0.0
        sum = 0.0
        for r in range(self.N):
            for c in range(self.N):
                for k in range(self.N):
                    sum = (sum + self.TM[r][k] * self.T[k][c])
                self.fin[r][c] = int(sum)
                sum = 0.0

    def CalculateQ(self):
        temp = 0
        print("Quality Selected: {0}".format(self.Qlevel))
        if self.Qlevel == 50:
            self.Q_Mat = np.copy(self.Q50)
        elif (self.Qlevel >= 1) and (self.Qlevel < 50):
            for r in range(self.N):
                for c in range(self.N):
                    temp = int(self.Q50[r][c] * (50 / self.Qlevel))
                    if (temp > 255):
                        self.Q_Mat[r][c] = 255
                    else:
                        self.Q_Mat[r][c] = int(round(self.Q50[r][c] * (50 / float(self.Qlevel))))

        elif (self.Qlevel > 50) and (self.Qlevel <= 100):
            for r in range(self.N):
                for c in range(self.N):
                    self.Q_Mat[r][c] = int(round(self.Q50[r][c] * ((100 - float(self.Qlevel)) / 50.0)))

                    # int(round(self.Q50[r][c] * (100-(float(self.Qlevel)/50.0))))

        else:
            print("An invalid quantisation level was entered")
        self.printMatrix(self.Q_Mat, 1)

    def Generate_T(self):
        print("Matrix T")
        for r in range(self.N):
            for c in range(self.N):
                if (r == 0):
                    self.T[r][c] = 1 / math.sqrt(self.n)
                else:
                    self.T[r][c] = math.sqrt((2.0 / self.n)) * math.cos((r * math.pi * (2 * c + 1)) / (2 * self.n))
                self.Tt[c][r] = self.T[r][c]
        """self.printMatrix(self.T, 0)
        print("\n\nT-Transposed")
        self.printMatrix(self.Tt, 0)"""

    def printMatrix(self, npArray, type):
        if type == 0:
            for r in range(self.N):
                print(" "),
                for c in range(self.N):
                    print("{0:0.3f}".format(npArray[r][c]), end=' ')
        if type == 1:
            for r in range(self.N):
                print(" "),
                for c in range(self.N):
                    print("{0}".format(npArray[r][c]), end=' ')

    def QuantizationStepForward(self):

        #self.C = np.divide(self.DCT, self.Q_Mat)

        for r in range(self.N):
            for c in range(self.N):
                self.C[r][c] = round(self.DCT[r][c] / self.Q_Mat[r][c])


    def QuantizationStepInverse(self):

        #self.R = np.multiply(self.C, self.Q_Mat)

        for r in range(self.N):
            for c in range(self.N):
                self.R[r][c] = round(self.C[r][c] * self.Q_Mat[r][c])

    def Compare(self):
        dif = np.abs(np.subtract(self.M, self.fin))
        print("\n\nDifference\n")
        print(dif)

