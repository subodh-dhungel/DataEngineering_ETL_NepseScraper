# 4.You need to perform matrix and linear algebra operations, such as matrix multiplication,
# finding determinants, solving linear equations, and so on. (explore numpy).

import numpy as np

class MatrixOperations:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def multiplyMatrix(self, otherMatrix):
        otherMatrix = np.array(otherMatrix)
        return np.dot(self.matrix, otherMatrix)

    def findDeterminant(self):
        return np.linalg.det(self.matrix)

    def solveLinearEquations(self, b):
        b = np.array(b)
        return np.linalg.solve(self.matrix, b)

    def transposeMatrix(self):
        return self.matrix.T

matrixA = [[2, 3], [1, 4]]
matrixB = [[5, 2], [3, 6]]
vectorB = [5, 7]

operations = MatrixOperations(matrixA)

# Matrix multiplication
resultMultiplication = operations.multiplyMatrix(matrixB)
print("Matrix Multiplication Result:\n", resultMultiplication)

# Determinant of matrix
determinant = operations.findDeterminant()
print("Determinant of matrix:", determinant)

# Solving linear equations Ax = B
solution = operations.solveLinearEquations(vectorB)
print("Solution to linear equations:", solution)

# Transpose of matrix
transposedMatrix = operations.transposeMatrix()
print("Transposed Matrix:\n", transposedMatrix)