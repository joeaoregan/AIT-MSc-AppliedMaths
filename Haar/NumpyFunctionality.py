import numpy as np

identityMatrix = np.eye(3)
print("Identity Matrix")
print(identityMatrix)

data = [[1,2,3],[4,5,6],[7,8,9]]
print("Matrix B")
print(data)
kron = np.kron(data, identityMatrix)
print("\nronenecker Product\n")
print(kron)

mat1 = [[1,2], [3,4]]
mat2 = [[5,6,7],[8,9,10],[11,12,13]]
kron2 = np.kron(mat1, mat2)
print("\nMatrix A")
print(mat1)
print("\nMatrix B")
print(mat2)
print("\nKronenecker Product\n")
print(kron2)

RanMat1 = np.random.randint(10, size=(np.random.randint(1,8), np.random.randint(1,8)))
RanMat2 = [[5,6,7],[8,9,10],[11,12,13]]
kron3 = np.kron(RanMat1, RanMat2)
print("\nMatrix A")
print(RanMat1)
print("\nMatrix B")
print(RanMat2)
print("\nKronenecker Product\n")
print(kron3)
