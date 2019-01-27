def fibo(n):
    if n<=1:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))
if __name__ == '__main__':
    x=int(input("Enter a number "))
    for i in range(x):
        print(fibo(i))
