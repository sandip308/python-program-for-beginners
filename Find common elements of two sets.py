x=set(eval(i) for i in input("Enter few elements ").split(','))
y=set(eval(i) for i in input("Enter few elements ").split(','))
s=x.intersection(y)
if s==set():
    print("No common elements found")
else:
    print("The common elements are:",s)

