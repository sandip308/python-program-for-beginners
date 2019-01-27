x=int(input("Enter a number "))
c=1
fac=1
if(x>=0):
    while (x >= c):
        fac = fac * x
        x = x - 1
    print(fac)
else:
    print("Enter right number ")