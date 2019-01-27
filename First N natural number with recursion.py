def natural(l,u):
    if l>u:
        return
    else:
        print(l,end=",")
        natural (l+1,u)

if __name__ == '__main__':
    x = int(input("Enter a lower limit of natural number "))
    y= int(input("Enter a upper limit of natural number "))
    natural(x,y)
