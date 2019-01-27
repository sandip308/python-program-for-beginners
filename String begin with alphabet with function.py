def begin_alphabet(n):
    w={}
    print("Give words according to the list of string ")
    for i in n:
        w[i]=input()
    return w
if __name__ == '__main__':
    x=list(str(i) for i in input("Enter some alphabet ").split(','))
    print(begin_alphabet(x))