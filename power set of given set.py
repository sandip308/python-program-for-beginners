try:
    x = list(eval(e) for e in input("Enter some value ").split(','))
    ps=[[]]
    for i in x:
        for j in ps:
            ps=ps+[list(j)+[i]]
    print(ps)
except:
    print("There are some problem")