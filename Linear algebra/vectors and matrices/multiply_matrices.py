import numpy as np

A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
 
# take a 3x4 matrix
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]
 
# result will be 3x4
 
result= [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

result = np.dot(A,B)
for r in result:
    print(r)
    
# Using recursive matrix multiplication
'''Algorithm:

Check if the dimensions of the two input matrices are valid for multiplication. If the number of columns in the first matrix does not equal the number of rows in the second matrix, then they cannot be multiplied. In this case, raise an error or return a None object.
Check if the matrices are of size 1×1. If they are, multiply their elements and return the result.
If the matrices are not of size 1×1, divide each matrix into four submatrices of equal size.
Recursively multiply the submatrices using the same algorithm, until each submatrix is of size 1×1.
Compute the product of the resulting submatrices using the formula:
result = [A11B11 + A12B21, A11B12 + A12B22, A21B11 + A22B21, A21B12 + A22B22]
Return the resulting matrix.'''

def multiply_matrix(a,b):
    if len(a[0] != len(b)):
        raise ValueError("Invalid matrix dimensions")
    
    results = [[0 for j in range(len(b[0]))] for i in range(len(a))]
    
    def multiply(a,b,results,i,j,k):
        if i >= len(a):
            return
        if j>= len(b[0]):
            return multiply(a, b, result, i+1, 0, 0)
        if k>= len(b):
            return multiply(a,b,results, i, j+1,0)
        
        results[i][j] += a[i][j] * b[k][j]
        multiply(a,b,results,i,j,k)

    multiply(a,b,results,0,0,0)
    return results          
a = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
b = [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]

results = multiply_matrix(a,b)
for row in results:
    print(row)