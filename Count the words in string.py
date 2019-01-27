def count_word(n):
    c=0
    for i in n:
        c+=1
    return c
if __name__ == '__main__':
    str=input("Enter a string : ")
    print("The number of the words in this string is=",count_word(str))