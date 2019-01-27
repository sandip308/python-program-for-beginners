from numpy import*
r= int(input("Enter row value :"))
c=int(input("Enter column value :"))
mat=[]
for i in range(r):
    mat.append([])
for i in range(r):
    for j in range(c):
        mat[i].append(j)
for i in range(r):
    for j in range(c):
        mat[i][j]=int(input())
x=reshape(matrix(mat),(r,c))
print("The original matrix is :")
print(x)
print("The transpose matrix is-> ")
y=x.transpose()
print(y)

