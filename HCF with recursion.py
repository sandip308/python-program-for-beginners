def HCF(f,s):
    if s==0:
        return f
    else:
        return HCF(s,f%s)
if __name__ == '__main__':
    r = int(input("Enter a first number "))
    c = int(input("Enter second number "))
    if r >= c:
        z = HCF(r, c)
        print("The HCF value is=",z)
    else:
        z = HCF(c, r)
        print("The HCF value is=",z)
