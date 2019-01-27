x=input("Enter a string ")
y=input("Enter a pattern string ")
if y in x:
    z = x.count(y)
    print("Match found,occourrence is",z)
else:
    print("Match not found")
