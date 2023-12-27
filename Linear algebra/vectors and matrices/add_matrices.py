
x= [[1,2,3],
    [4,5,6,],
    [7,8,9]]

y= [[9,8,7],
    [6,5,4],
    [3,2,1,]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(x)):
    # iterate through columns
    for j in range(len(x[0])):
        result[i][j]=x[i][j] + y[i][j]
        
# for printing result through iterating
for r in result:
    print(r)


# add matrices using numpy

import numpy as np

X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
  
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

#  sumation = np.add(X,Y)  by add() method.
result = np.array(X) + np.array(Y)
print(result)

# add two matrices using sympy
import sympy as Matrix

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
 
b = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

# create Matrix objects from the lists
matrix_a = Matrix(a)
matrix_b = Matrix(b)

results = matrix_a + matrix_b
print(results) 