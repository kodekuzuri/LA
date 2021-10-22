import numpy as np 

# (a)
i = -1/np.sqrt(2)
A = np.array([[i, 0.00], [0.00, i], [-1.00, 1.00]])

print("Array A: ")
print(A)
print(f"Conditional number(A) = {np.linalg.cond(A)} ")
print("")

# (b)
A = np.array([[-2, 1, 2], [0, 2, 0]])

print("Array A: ")
print(A)
print(f"Conditional number(A) = {np.linalg.cond(A)} ")
print("")


#(c)
A = np.array([[1.0, 0.9], [0.9, 0.8]])
print("Array A: ")
print(A)
print(f"Conditional number(A) = {np.linalg.cond(A)} ")
modA = np.linalg.det(A)

if modA == 0:
    print("Matrix is not invertible")
else :
    print("Matrix is invertible")

print(f"Determinant(A) = {modA}")
print("")

#(d)
A = np.array([[1, 0], [0, -10]])
print("Array A: ")
print(A)
print(f"Conditional number(A) = {np.linalg.cond(A)} ")
modA = np.linalg.det(A)

if modA == 0:
    print("Matrix is not invertible")
else :
    print("Matrix is invertible")

print(f"Determinant(A) = {modA}")
print("")

# (e)
epsn = np.array([10.00, 5.00, 1.00, 1e-1, 1e-2, 1e-4, 0.00])

for i in epsn:
    A = np.array([[1.00, 1.00], [1.00, i]])
    print("Array A: ")
    print(A)
    print(f"Conditional number(A) = {np.linalg.cond(A)} ")
    modA = np.linalg.det(A)

    if modA == 0:
        print("Matrix is not invertible")
    else :
        print("Matrix is invertible")

    print(f"Determinant(A) = {modA}")
    print("")
