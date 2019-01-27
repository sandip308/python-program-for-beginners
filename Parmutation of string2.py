def parmutaion(str,s):
    if len(str)==s:
        print(''.join(str))
    else:
        for i in range(s,len(str)):
            str_copy=[c for c in str]
            str_copy[s], str_copy[i] = str_copy[i], str_copy[s]  #swap the character
            parmutaion(str_copy,s+1)
if __name__ == '__main__':
    x=input("Enter a string ")
    parmutaion(x,0)