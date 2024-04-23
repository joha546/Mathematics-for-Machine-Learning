'''The multiplication of two matrices Am*n and Bn*p give a matrix Cm*p. It means a number of columns in A must be equal to the number of 
rows in B to calculate C=A*B. To calculate element c11,

The complexity of multiplication operation (A*B) is O(m*n*p) where m*n and n*p are the order of A and B respectively'''



# Python code for matrix multiplication
a = [[2, 5], [1, 7]]
b = [[3, 7], [2, 9]]
c = [[0, 0], [0, 0]]
for i in range(0, 2):
    for j in range(0, 2):
        c[i][j] = 0
        for k in range(0, 2):
            c[i][j] = c[i][j]+(a[i][k]*b[k][j])
for i in range(0, 2):
    for j in range(0, 2):
        print(c[i][j])
 
        # This code is contributed by ishankhandelwals.