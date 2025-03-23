# Implement concatenation of arrays

import array as arr
array1=arr.array('d',[1,3,5,7,9])
array2=arr.array('d',[2,4,6,8,10])

#1st way
array3=array1+array2
print(array3)

#2nd way (merges array2 in array1 itself)
array1.extend(array2)
print(array1)


# Find the length of arrays

#1st way
flag=0
for i in array1:
    flag+=1
print(f"The length of the array would be: {flag}")

#2nd way (using length function)
print(f"The length of the array would be: {len(array1)}")

#3rd way (sorting and then finding the index of the last element)
arr_sorted=sorted(array1)
print(array1.index(max(arr_sorted))+1) #This will fail if repitition of max values is there



