x=int(input("Enter a number"))
y=int(input("Enter another number"))
if x>y:
    l=x*y
    r=x%y
    while r!=0 :
        x=y
        y=r
        r=x%y
    print("The gcd number is= ",y)
    print("The lcm number is=",l//y)
else:
    v=x*y
    r = y % x
    while r != 0:
        y = x
        x = r
        r = y % x
    print("The gcd number is=",x)
    print("The lcm number is=",v//x)