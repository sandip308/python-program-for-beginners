x=int(input("Enter a number "))
import random
sum=0
for i in range(x):
    x=random.randint(1,6)
    y=random.randint(1,6)
    sum=x+y
    print("%d'th chance sum is= %d"%(i+1,sum))