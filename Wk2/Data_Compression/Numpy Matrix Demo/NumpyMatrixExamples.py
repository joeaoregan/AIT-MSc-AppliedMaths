import numpy as np
import random
import matplotlib.pyplot as plt

print("Creating and printing 2 x 2D arrays using numpy")
a = np.array([[3,-1,4],[0,5,-2],[6,7,8]])
b = np.array([[1,2,-4],[4,-3,-2],[3,6,0]])
print("Matrix A:\n {0}". format(a))
print("Matrix B:\n {0}". format(b))

print("\n\nPreforming an element wise multiplication of these arrays yields")
c = (np.multiply(a,b))
print(c)

print("\n\nThe product of Matrix A and Matrix B arrays yields")
c = (np.matmul(a,b))
print(c)
#print(np.divide(a, b))

print("\n\nCreate a random Matrix of MXN dimensions conisting of floats between 0 and 1 ")
d = np.random.rand(3,5)
print(d)

print("\n\nCreate a random Matrix of MXN dimensions conisting of floats between 0 and 1 ")
d = np.random.rand(3,5)
print(d)

"""The following section of code looks at generating random data and visualising the 
results using plots"""


print("\n\nThe following loop iterates through and prints the contents of a 2D array of random integers")
d = np.random.random_integers(random.randint(1,10), size=(random.randint(3,10),random.randint(3,10)))

rows = np.size(d,0)
cols = np.size(d, 1)
print("Number of rows: {0}\nNumber of columns: {1}" .format(rows, cols))
for r in range(rows):
    print(" "),
    for c in range(cols):
        print("{0}".format(d[r][c]), end=' ')


plt.imshow(d, 'gray')
plt.show()

