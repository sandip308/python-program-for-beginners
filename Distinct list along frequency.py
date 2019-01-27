x=eval(input("Enter a list along wth [] "))
for l in x:
    print(l)
y=eval(input("Enter a number which frequency u want to be search"))
c=0
f=0
for l in x:
    if y==l:
        c=c+1
        f=1
if f==1:
    print("Number of frequency is=",c)
else:
    print("No such item found in list")

