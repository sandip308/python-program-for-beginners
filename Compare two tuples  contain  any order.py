t=tuple(eval(x)for x in input("Enter some values ").split(","))
v=tuple(eval(x)for x in input("Enter some values ").split(","))
a=sorted(t,reverse=False)
b=sorted(v,reverse=False)
if a==b:
    print("Elements are same ")
else:
    print("Elements are not same")