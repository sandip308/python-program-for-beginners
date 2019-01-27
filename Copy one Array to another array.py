from array import*
arr1 =array('i',[23,45,67])
arr2=array(arr1.typecode,(a for a in arr1))
for a in arr2:
    print(a)
