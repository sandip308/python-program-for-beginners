try:
    from functools import reduce
    x=[int(i) for i in input("Enter some value ").split(',')]
    z=list(filter(lambda n: n%2==0 ,x))
    c=reduce(lambda a,b:a+b,z)
    print("Sum of all even number in this list is=",c)
    y=list(filter(lambda n: n%2!=0,x))
    print("Sum of all odd numbers in this list is=",reduce(lambda a,b:a+b,y))
except TypeError:
    print("please give all intiger value ")
except:
    print("There are some problem arise ")