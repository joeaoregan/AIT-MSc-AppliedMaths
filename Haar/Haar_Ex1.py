from pywt import wavedec
import pywt
#https://pywavelets.readthedocs.io/en/latest/regression/wavelet.html?highlight=haar

def printDetails():
    print("Family of wavelets available:")
    print(pywt.families())
    print("\n{0}".format(pywt.Wavelet('haar')))

def Example1():
    data = [1,2,3,4,5,6,7,8]
    cA, cD = pywt.dwt(data, 'haar')
    print('\n----------Example 2 (Single Level)----------')
    print("Data: {0}".format(data))
    print("Average: {0}".format(cA[0]))
    print("Mother Wavelet: {0}".format(cA[1]))
    print("Wavelets at 2^1: {0}, {1}".format(cA[2], cA[3]))
    print("Wavelets at 2^2: {0}".format(cD))

def Example2():
    data = [1,2,3,4,5,6,7,8]
    coeffs = wavedec(data, 'haar', level=3)
    cA, cD3, cD2, cD1 = coeffs
    print('\n----------Example 3 (Full Decomp)----------')
    print("Data: {0}".format(data))
    print("Overall Average: {0}".format(cA))
    print("Mother Wavelet: {0}".format(cD3))
    print("Wavelets at 2^1: {0}".format(cD2))
    print("Wavelets at 2^2: {0}".format(cD1))

def main():
    printDetails()
    Example1()
    Example2()


if __name__=="__main__":
    main()



def Example3():
    data = [1,2,3,4]
    cA, cD = pywt.dwt(data, 'haar')
    print('\n----------Example 1 (Single Level)----------')
    print("Data: {0}".format(data))
    print("Average: {0}".format(cA[0]))
    print("Mother Wavelet: {0}".format(cA[1]))
    print("Wavelets at 2^1: {0}".format(cD))