x=int(input("Enter a lower number "))
y=int(input("Enter a grater number "))
if x<y:
    for i in range(x,y+1):
        c=0
        for j in range (1,i+1):
            if i%j==0:
                c=c+1
        if c==2:
            print(i)
else:
    print("You entered wrong range ")

