import numpy as np
import math

np.set_printoptions(suppress=True)

N = 8
m = np.array([[16, 8, 23, 16, 5, 14, 7, 22],
              [20, 14, 22, 7, 14, 22, 24, 6],
              [15, 23, 24, 23, 9, 6, 6, 20],
              [14, 8, 11, 14, 12, 12, 25, 10],
              [10, 9, 11, 9, 13, 19, 5, 17],
              [8, 22, 20, 15, 12, 8, 22, 17],
              [24, 22, 17, 12, 18, 11, 23, 14],
              [21, 25, 15, 16, 23, 14, 22, 22]])

Q50 = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                [12, 12, 14, 19, 26, 58, 60, 55],
                [14, 13, 16, 24, 40, 57, 69, 56],
                [14, 17, 22, 29, 51, 87, 80, 62],
                [18, 22, 37, 56, 68, 109, 103, 77],
                [24, 35, 55, 64, 81, 104, 113, 92],
                [49, 64, 78, 87, 103, 121, 120, 101],
                [72, 92, 95, 98, 112, 100, 103, 99]])
T = np.zeros((N, N), dtype='float')
Q = np.zeros((N, N), dtype='float')


def calculateT():
    for r in range(N):
        for c in range(N):
            if (r == 0):
                T[r][c] = 1 / math.sqrt(N)
            else:
                T[r][c] = (math.sqrt((2.0 / N)) * math.cos((r * math.pi * (2 * c + 1)) / (2 * N)))


def main():
    # Compression

    print("\nData to be compressed:\n")
    print(m)
    calculateT()
    T2 = T.round(2)
    TM = np.matmul(T2, m)
    t = T2.transpose()
    D = np.matmul(TM, t)

    q = int(input("\n\n\nSelect Quantisation Level (integer values only): "))
    if (q > 50):
        Q = np.multiply(Q50, (100.0 - q) / 50.0)
    else:
        Q = np.multiply(Q50, 50 / q)

    for r in range(N):
        for c in range(N):
            if (Q[r][c] > 255):
                Q[r][c] = 255

    C = (np.divide(D, Q))

    print("\nCompressed data:\n")
    print(C.round())

    # Decompression

    R = np.multiply(Q, C)
    tR = np.matmul(t, R)
    TRt = np.matmul(tR, T2)

    print("\nDecompressed data:\n")
    print(TRt.round())

    print("\nDifference:\n")
    temp = np.abs(np.subtract(m, TRt))
    print(temp.round())
    print(temp.mean())


if __name__ == "__main__":
    main()
