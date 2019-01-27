def sum_of_digit(n):
    if n==0:
        return 0
    else:
        x=n%10
        return x + sum_of_digit(n//10)
if __name__ == '__main__':
    x=int(input("Enter a number "))
    print("Sum of digits is=",sum_of_digit(x))