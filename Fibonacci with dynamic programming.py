def fibo(n):
    l=[-1]*(n+1)
    if l[n] != -1:
        return l[n]
    elif n==0:
        l[n]=0
        return l[n]
    elif n==1:
        l[n] = 1
        return l[n]
    else:
        l[n]= fibo(n-1) + fibo(n-2)
        return l[n]
if __name__ == '__main__':
    x=int(input("Enter a number "))
    print(fibo(x))