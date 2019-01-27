x=eval(input("Enter a list along with [] "))
s=0
sum=0
for i in x:
    if i%2==0:
        s=s+i
    else:
        sum=sum+i
print("The odd number sum in this list is=",sum)
print("The even number sum in this list is=",s)