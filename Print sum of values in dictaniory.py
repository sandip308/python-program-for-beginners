try:
    x={i:int(input("value is: ")) for i in range(3)}
    s=0
    for z in x.values():
       s=s+z
    print("sum is: ",s)
except:
    print("There are some error...Try again")