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

def RunNumericalExample(N, haar, normFlag):
    size = np.size(haar)
    reCompData = np.zeros(size)
    decompData = np.zeros(size)
    haar = haarMatrix(N, normFlag)
    np.set_printoptions(precision=3)
    print("*******   Haar Decomposition   *******")
    #data = np.random.randint(1,100,(1,N)).ravel()
    data = [1, 2, 3, 4, 5, 6, 7, 8]
    print("Data: {0}".format(data))
    if normFlag==True:
        decompData = (np.matmul(haar, data))/(math.sqrt(N))
        for v in decompData:
            print("{0:0.3f}".format(v)),
        print("*******   ------------------   *******")
    else:
        print("The Haar matrix required by the Haar transform should be normalized.\n"
              "This wont work, sorry......")
    haar = np.transpose(haar)
    if normFlag==True:
        reCompData = ((np.matmul(haar, decompData)) / (math.sqrt(N)))
        print("*******   Haar Recomposition   *******")
        print(reCompData)
        print("*******   ------------------   *******")
    else:
        print()

def main():
    N=8
    normFlag = True
    haar = haarMatrix(N, normFlag)
    np.set_printoptions(precision=3)
    print("*******   Haar Transform Matrix (N={0})   *******".format(N))
    print(haar)
    print("*******   --------------------------   *******".format(N))
    RunNumericalExample(N, haar, normFlag)

if __name__=="__main__":
    main()