def lcm_number(r,c):
    rem=r%c
    while rem !=0:
        r=c
        c=rem
        rem=r%c
    return c
if __name__ == '__main__':
    r = int(input("Enter a first number "))
    c = int(input("Enter second number "))
    if r>=c:
        z=lcm_number(r,c)
        print("The lcm number of two number is=",(r*c)//z)
    else:
        z=lcm_number(c,r)
        print("The lcm number of two number is=", (r * c) // z)