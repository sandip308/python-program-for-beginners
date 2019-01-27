def square(l,u):
    if l>u:
        return
    else:
        print(l*l)
        square(l+1,u)
if __name__ == '__main__':

    try:
        x=int(input("Enter a lower range "))
        y=int(input("Enter a upper range "))
        if x<y:
            square(x,y)
        else:
            square(y,x)
    except TypeError:
        print("Please enter integer value ")
    except:
        print("There are some problem arise ")