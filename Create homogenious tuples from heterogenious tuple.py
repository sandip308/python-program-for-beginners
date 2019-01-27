t=tuple(eval(x)for x in input("Enter some values ").split(","))
for i in t:
    if type(i)==int:
        print(i,end=" ")
    else:
        pass