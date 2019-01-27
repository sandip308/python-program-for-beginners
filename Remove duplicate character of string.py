x=input("Enter a string ")
y=input("Enter a string whose duplicate to be remove ")
z=x.count(y)
if z>=2:
    x=x.replace(y,'')
    print(x)
else:
    print("There are no duplicate character ")