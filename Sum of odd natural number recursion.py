def odd_number(p):
    if p <= 0:
        return 0
    else:
        return 2*p-1 + odd_number(p-1)

x = int(input("Enter a range "))
print("Sum of all odd number in a given range is=", odd_number(x))
