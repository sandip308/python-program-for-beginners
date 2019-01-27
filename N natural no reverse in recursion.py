def reverse(n):
    if n==0:
        return
    else:
        print(n)
        return (reverse(n-1))
if __name__ == '__main__':
    x=int(input("Enter a range "))
    reverse(x)