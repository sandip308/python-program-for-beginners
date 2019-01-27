x=input("Enter a string ")
c=0
f=0
for i in x:
    if(i=='0'or i=='1'or i=='2'or i=='3'or i=='4'or i=='5'or i=='6'or i=='7'or i=='8'or i=='9' ):
        f=1
        c=c+1
if f==1:
    print("Numbers of the words in this string is=",c)
else:
    print("There are no numbers in this string ")