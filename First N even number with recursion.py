def even(l,u):
    if l>u:
        return
    else:
        if l%2==0:
            print(l,end=",")
        even(l+1,u)
if __name__ == '__main__':

    try:
        x=int(input("Enter a lower range "))
        y=int(input("Enter a upper range "))
        if x<y:
            even(x,y)
        else:
            even(y,x)
    except TypeError:
        print("Please enter integer value ")
    except:
        print("There are some problem arise ")