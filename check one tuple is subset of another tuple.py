t=tuple(eval(x)for x in input("Enter some values ").split(","))
v=tuple(eval(x)for x in input("Enter some values ").split(","))
l=set(t)
s=l.issubset(v)
if s==True:
    print("First tuple is subset of second tuple")
else:
    print("First tuple is not subset of second tuple")