def sum(n):
    s=0
    if n==0:
        return 0
    else:
        s= n+sum(n-1)
        return s
if __name__ == '__main__':
    try:
        v=int(input("Enter a number "))
        z=sum(v)
        print("Sum of all integer is=",z)
    except TypeError:
        print("Please enter integer value ")
    except:
        print("There are some problem arise ")
