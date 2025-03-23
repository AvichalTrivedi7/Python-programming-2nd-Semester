import array as arr
import random as ran

list1=eval(input("Enter the array of integers: "))
deleted_elements=[]
array1 = arr.array("i",list1)

def erase(a):
    if len(a)<5:
        a.clear()
        print(f"The array does not have enough elements, emptying the array instead, array ---> {array1}")
    else:
        for i in range(5):
            r=ran.randint(0,len(a)-1)
            deleted_elements.append(a.pop(r))
        print(f"The randomly deleted elements from the array are ---> {deleted_elements}")
        print(f"The array with remaining elements ---> {array1}")
    

erase(array1)