# Haar Tutorial Questions
# Q3
import numpy as np
import math

def haarMatrix(n, normalised):
    n = 2**np.ceil(np.log2(n))  # Allow only size n of power 2
    if n > 2:
        h = haarMatrix(n / 2, normalised)
    else:
        return np.array([[1, 1], [1, -1]])
    h_n = np.kron(h, [1, 1])    # calculate upper haar part
    if normalised:              # calculate lower haar part
        h_i = np.sqrt(n/2)*np.kron(np.eye(len(h)), [1, -1])
    else:
        h_i = np.kron(np.eye(len(h)), [1, -1])
    h = np.vstack((h_n, h_i))   # combine parts
    return h

def main():
    N=8
    haar = haarMatrix(N, True)
    np.set_printoptions(precision=5)
    print(haar)
    data = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0]
    output = (np.matmul(haar, data))/(math.sqrt(N))
    for v in output:
        print(v),

if __name__=="__main__":
    main()
