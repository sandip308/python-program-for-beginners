from numpy import *
r1=int(input("Enter matrix1 row value: "))
c1=int(input("Enter matrix1 column value: "))
r2=int(input("Enter matrix2 row value: "))
c2=int(input("Enter matrix2 column value: "))
matrix1=[]
for i in range(r1):
    matrix1.append([])
for i in range(r1):
    for j in range(c1):
        matrix1[i].append(j)
print("Enter the matrix1 elements:")
for i in range(r1):
    for j in range(c1):
        matrix1[i][j]=int(input())
x=reshape(matrix(matrix1),(r1,c1))
matrix2=[]
for i in range(r2):
    matrix2.append([])
for i in range(r2):
    for j in range(c2):
        matrix2[i].append(j)
print("Enter the matrix2 elements:")
for i in range(r2):
    for j in range(c2):
        matrix2[i][j]=int(input())
y=reshape(matrix(matrix2),(r2,c2))
z=x*y
print("The multiplication of this matrix is:->")
print(z)
