import numpy as np  # answer is in plot title of graph
import matplotlib.pyplot as plt
from matplotlib import rcParams

def Odd(k, b, L, t):    # t is the time that changes
    result = 0  # set result to 0
    if k<=0:
        return result
    result+= (b/(k*np.pi))*np.sin((k*np.pi/L)*t)+Odd(k-2,b, L, t)   # 20 / kPi(Sin(kPi/L * t), call function again - only thing that changes is the term number
    return result       # done for just one point at this time

def oddExample(data):
    k = int(input("Enter the number of terms you want - odd number only: "))    # enter odd number of terms
    L = 5.0                                                                     # upper limit of 5
    a0 = 14.0
    LL = -L # lower limit = -L
    UL = L  # upper limit
    b = 20  # in the example it was 4/kPi, this is calculated for us, likelihood is these values won't change, needed for every one of them
    step = 0.025
    size = int((np.absolute(LL)+np.absolute(UL))/step)+1
    print(size)

    x_data = []
    y_data = []

    text_file = open("Odd_Fourier_Data.csv", "w")  # as we calc each point in the series, put in texxt file
    for i in range(size):
        x_data.append(LL)                       # append with position on the limit
        y_data.append(a0/2+Odd(k,b,L,LL))       # a0 = dc average, k = num terms, b = 20, limits -- appended to y axis at the same point time is appended
        text_file.write("{0:0.5f} , {1:0.5f} \n".format(LL, Odd(k, b, L, LL)))  # write to text file, start at 5 and increase as we go
        LL+=step
    text_file.close()

    print("Plotting Step Function")
    x, y = data             # take in x & y data from original file
    """x = [-5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5]
    y = [2, 2, 2, 2, 2, 2, 12, 12, 12, 12, 12, 12]"""
    rcParams['axes.titlepad'] = 15
    plt.title(r"f(t) = %d+$\sum_{k=0}^\infty$$\frac{%d}{k\pi}\sin\left(\frac{k\pi}{%d}t\right) $ (k=%d)"%((a0/2),b,L,k))    # hint at answer, can write formula directly into title - specifies number of terms
    plt.plot(x, y, linewidth=3)
    plt.plot(x_data, y_data, linewidth=3)
    plt.grid(True)
    plt.savefig("Odd_Square_Wave.png")
    plt.show()


def loadData():     # no need for option here
    x, y = np.genfromtxt('Odd_Data.csv', unpack=True, delimiter=',')    # open csv file, comma used as delimiter to separate data
    return (x, y)   # x into x array, y into y array

def main():
    print("Fourier Series Plots")
    oddExample(loadData())      # no need to input 1


if __name__=="__main__":
    main()
