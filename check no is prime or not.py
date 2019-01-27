x=int(input("Enter a number: "))
c=2
flag=0
if(x>0):
    while x>c:
        if x%c==0:
            flag=1
            break
        c=c+1
    if(flag==1):
        print("The number is not a prime number")
    else:
        print("The number is a prime number")
else:
    print("You enter wrong number ")
