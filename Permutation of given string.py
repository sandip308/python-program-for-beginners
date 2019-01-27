from itertools import permutations
def permutation(str):
    prem=permutations(str)
    for i in list(prem):
        print(''.join(i))

if __name__ == '__main__':
    x=input("Enter a string ")
    permutation(x)