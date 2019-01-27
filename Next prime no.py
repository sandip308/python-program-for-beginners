x=int(input("Enter a number "))
for i in range(x+1,2*x):
    flag = 0
    for num in range(2,i):
        if i%num==0:
            flag=1
            break
    if flag==0:
        print("Next prime number is=",i)
        break