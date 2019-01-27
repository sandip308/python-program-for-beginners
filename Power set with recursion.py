def power_set(n):
    if not n:
        return [[]]
    else:
        z=[[n[0]]+ c for c in power_set(n[1:])]
        v = power_set(n[1:])
        return z + v

if __name__ == '__main__':
    x=list(int(a) for a in input("Enter some elements : ").split(','))
    print(power_set(x))