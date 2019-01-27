t=tuple(int(x)for x in input("Enter three values ").split(","))
sum=0
for y in t:
    sum=sum+y
if len(t)==0:
    print("Invalid length of tuple ")
else:
    avg=sum/len(t)
    print("The average is =",avg)