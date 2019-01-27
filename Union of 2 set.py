try:
    x = set(eval(e) for e in input("Enter some value ").split(','))
    y = set(eval(e) for e in input("Enter some others value ").split(','))
    s=x.union(y)
    print("The union of this set is=",s)
except SyntaxError:
    print("There are some problem please try again")
else:
    print("Thank You")