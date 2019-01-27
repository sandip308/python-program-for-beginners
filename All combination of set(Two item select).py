def combination(n):
    s=[]
    for i in n:
        for j in n:
            s.append([i]+[j])
    return s
if __name__ == '__main__':
    try:
        x=set(int(i) for i in input("Enter some value ").split(','))
        v=combination(x)
        print(v)
    except:
        print("There are some problem ")