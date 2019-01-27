def fibonacci(n):
    a,b,c=0,1,0
    print("The fibonacci series is->")
    print(a)
    count=1
    while count<n:
        c=a+b
        b=a
        a=c
        print(c)
        count+=1
if __name__ == '__main__':
    x=int(input("Enter a number(How much fibonacci will you print ): "))
    fibonacci(x)
