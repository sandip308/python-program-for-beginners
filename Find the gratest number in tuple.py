x=tuple(int(x) for x in input("Enter some value ").split(','))
a=sorted(x,reverse=True)
for i in a:
    print("The greatest number is =",i)
    break