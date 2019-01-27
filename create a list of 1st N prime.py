x=int(input("Enter a range "))
s=[]
for i in range(1,x+1):
    c=0
    for j in  range(1,i+1):
        if i%j==0:
          c=c+1
    if c==2:
      s.append(i)
for m in s:
    print(m,end=" ")