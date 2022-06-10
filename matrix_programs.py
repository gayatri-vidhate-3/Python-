'''#Q1 Python program to add two Matrices
X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

#USING FOR LOOP
result = [[0,0,0],
        [0,0,0],
        [0,0,0]]

#print(len(X))
#print((X[0]))
#print(Y)

for i in range(len(X)):        # iterate through rows
    for j in range(len(X[0])):   #iterate through columns
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)

------------------------------------------------------------
#USing list comprehension
X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

print((X[0]))
print(len(X[0]))
result = [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

for r in result:
    print(r)

---------------------------------------------------------------------
#Using Zip
X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

result = [map(sum, zip(*t)) for t in zip(X, Y)]

print(result)
---------------------------------------------------------
#Q 2 Python program to multiply two matrices
X = [[1, 7, 3],
     [3, 5, 6],
     [6, 8, 9]]
Y = [[1, 1, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]
Output: [55, 65, 49, 5]
[57, 68, 72, 12]
[90, 107, 111, 21]

X = [[1, 7, 3],
     [3, 5, 6],
     [6, 8, 9]]
Y = [[1, 1, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]
result = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

print(len(X))
print(len(Y[0]))
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

for r in result:
    print(r)

#OR Matrix Multiplication (Vectorized implementation).
# this also gives same result but need to implement on jupyter
X = [[1, 7, 3],
     [3, 5, 6],
     [6, 8, 9]]
Y = [[1, 1, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]

result = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
import numpy as np
result = np.dot(X,Y)

for r in result:
    print(r)

------------------------------------------------------------------------
#Q3 Python program for Matrix Product
list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
print(list)
result = 1

for i in range(len(list)):
    for j in range(len(list[i])):
        result *= list[i][j]

print(result)
----------------------------------------------------------------------------'''