import numpy as np

print("Enter elements for 5x3 matrix:")
list1 = []
for i in range(5):
    row = list(map(int, input().split()))
    list1.append(row)

A = np.array(list1)

print("Enter elements for 3x2 matrix:")
list2 = []
for i in range(3):
    row = list(map(int, input().split()))
    list2.append(row)

B = np.array(list2)

print("Matrix A:")
print(A)

print("Matrix B:")
print(B)

# Multiply matrices
result = np.dot(A, B)

print("Product Matrix (A x B):")
print(result)