try:
    x = set(eval(e) for e in input("Enter some value ").split(','))
    print("The elements in this set is=",len(x))
except:
    print("There are some problem")