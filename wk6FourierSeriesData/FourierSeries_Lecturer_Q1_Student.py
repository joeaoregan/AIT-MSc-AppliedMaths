import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

def Odd(k, b, L, t):
    result = 0
    if k<=0:
        return result
    result+= (b/(k*np.pi))*np.sin((k*np.pi/L)*t)+Odd(k-2,b, L, t)
    return result

def oddExample(data):
    k = int(input("Enter the number of terms you want - odd number only: "))
    L = 5.0
    a0 = 14.0
    LL = -L
    UL = L
    b = 20
    step = 0.025
    size = int((np.absolute(LL)+np.absolute(UL))/step)+1
    print(size)

    x_data = []
    y_data = []

    text_file = open("Odd_Fourier_Data.csv", "w")
    for i in range(size):
        x_data.append(LL)
        y_data.append(a0/2+Odd(k,b,L,LL))
        text_file.write("{0:0.5f} , {1:0.5f} \n".format(LL, Odd(k, b, L, LL)))
        LL+=step
    text_file.close()

    print("Plotting Step Function")
    x, y = data
    """x = [-5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5]
    y = [2, 2, 2, 2, 2, 2, 12, 12, 12, 12, 12, 12]"""
    rcParams['axes.titlepad'] = 15
    plt.title(r"f(t) = %d+$\sum_{k=0}^\infty$$\frac{%d}{k\pi}\sin\left(\frac{k\pi}{%d}t\right) $ (k=%d)"%((a0/2),b,L,k))
    plt.plot(x, y, linewidth=3)
    plt.plot(x_data, y_data, linewidth=3)
    plt.grid(True)
    plt.savefig("Odd_Square_Wave.png")
    plt.show()


def loadData(option):
    x, y = np.genfromtxt('Odd_Data.csv', unpack=True, delimiter=',')
    return (x, y)

def main():
    print("Fourier Series Plots")
    oddExample(loadData(1))


if __name__=="__main__":
    main()