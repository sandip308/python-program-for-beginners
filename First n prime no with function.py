def prime(n):
    if n>0:
        print("The prime numbers in this given range are: ")
        for i in range(1,n+1):
            c=0
            for j in range(1,i+1):
                if i%j==0:
                    c=c+1
            if c==2:
                print(i,end=' ')
if __name__ == '__main__':
    x=int(input("Enter a range :"))
    prime(x)