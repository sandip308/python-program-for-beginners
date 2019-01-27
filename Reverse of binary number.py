def binary(a):
    x=bin(a)
    v=x[2::]
    num=int(v)
    print("The reverse of corresponding decimal number is=")
    rev=0
    while num>0:
        c=num%10
        rev=(rev*10)+c
        num=num//10
    print(rev)
if __name__ == '__main__':
    print("Enter a decimal number ")
    x=int(input())
    binary(x)