x=list(eval(i) for i in input("Enter some set value:").split(','))
y=list(eval(i) for i in input("Enter some set value:").split(','))
s=[]
for p in x:
    for j in y:
      s+=[[p]+[j]]
print(s)
