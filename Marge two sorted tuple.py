t=tuple(int(x)for x in input("Enter first  values ").split(","))
v=tuple(int(x)for x in input("Enter second  values ").split(","))
a=sorted(t,reverse=False)
b=sorted(v,reverse=False)
c=a+b
print("Two merged Tuple is=",c)
print("Sorted merge tuple is=",sorted(c,reverse=False))