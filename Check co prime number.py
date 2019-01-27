x=int(input("Enter a number"))
y=int(input("Enter another number"))
if x>y:
    r=x%y
    while r!=0 :
        x=y
        y=r
        r=x%y
    if y==1:
        print("The numbers are co prime number ")
    else:
        print("The number are not co prime number")
else:
    r = y % x
    while r != 0:
        y = x
        x = r
        r = y % x
    if x==1:
        print("The numbers are co prime number ")
    else:
        print("The number are not co prime number ")