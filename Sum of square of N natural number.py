def square_sum(l):
    if l==0:
        return 0
    else:
        return ((l*l)+square_sum(l-1))
if __name__ == '__main__':

    try:
        x=int(input("Enter a range "))
        z=square_sum(x)
        print("The square sum of all natural number is=",z)
    except TypeError:
        print("Please enter integer value ")
    except:
        print("There are some problem arise ")