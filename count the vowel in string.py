x=input("Enter a string ")
c=0
for i in x:
    if (i=='a'or i=='e'or i=='i'or i=='o'or i=='u'or i=="A" or i=="E" or i=="I" or i=="O" or i=="U"):
        c=c+1
print("The vowel in this string is=",c)