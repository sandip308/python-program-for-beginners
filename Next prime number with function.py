def nextprime(n):
    for i in range(n+1,(2*n+1)):
        flag = 0
        for j in range(2,i):
            if i%j==0:
               flag=1
               break
        if flag==0:
            return i
            break
if __name__ == '__main__':
    try:
        x = int(input("Enter a number "))
        if x>0:
            print("The next prime number is=",nextprime(x))
        else:
            print("Please enter positive number ")
    except TypeError:
        print("Please enter integer value ")
    except:
        print("There are some problem ")
