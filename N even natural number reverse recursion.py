def even_reverse(n):
    if n==0:
        return
    else:
        if n%2==0:
            print(n,end=",")
        even_reverse(n-1)

if __name__ == '__main__':
    try:
        x=int(input("Enter a range "))
        even_reverse(x)
    except TypeError:
        print("Please enter integer value ")
    except:
        print("There are some problem arise ")