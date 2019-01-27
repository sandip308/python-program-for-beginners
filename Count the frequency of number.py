t=tuple(int(x)for x in input("Enter some values ").split(","))
s=set(t)
for j in s:
    print(j, "Occours ",t.count(j) , "times")