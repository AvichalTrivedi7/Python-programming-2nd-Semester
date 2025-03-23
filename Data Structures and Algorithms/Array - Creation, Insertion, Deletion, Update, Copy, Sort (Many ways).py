#Creation
import array as arr
my_arr=arr.array('i',[5,15,10,30,25,20])
print(f"Created array is ---> {my_arr}")
print("\n")


#Insertion (Through Append)
my_arr.append(35)
print(f"Appended element in the array is 35 ---> {my_arr}")
print("\n")

#Insertion (Through Insert)
my_arr.insert(0,0)
print(f"Zero has been inserted in the array at first position (Zero index) ---> {my_arr}")
print("\n")

#Insertion (Through Extend)
my_arr.extend([1,2,3,4])
print(f"Array has been extended by [1,2,3,4] ---> {my_arr}")
print("\n")


#Deletion (Through Pop)

#(Deletion of last element)
print(f"Element Deleted ---> {my_arr.pop()}, Array after deletion of last element ---> {my_arr}")

#(Deletion of specified element)
print(f"Element Deleted ---> {my_arr.pop(8)}, Array after deletion of the element at 8th index ---> {my_arr}")
print("\n")

#Deletion (Through remove)
my_arr.remove(2) 
print(f"Element with the value '2' has been removed ---> {my_arr}")
print("\n")


#Update (Through Index Value)
my_arr[-1]=40
print(f"Last element has been updated to be 40 ---> {my_arr}")
print("\n")


#Copy
#1st way
x=arr.array('i')
x=my_arr
print(f"The copied array is {x}")
print("Both have same ids",id(x),id(my_arr))
#If we use the assignment operator, any change in one array will reflect in the other (same id)
print("\n")

#2nd way
y=my_arr.__copy__()
print(f"The copied array is {y}")
print("Both have different ids, this way",id(y),id(my_arr))
print("\n")

#3rd way
another_copy=arr.array(my_arr.typecode,my_arr)
print(f"The copied array is {another_copy}")
print("Both have different ids, this way",id(another_copy),id(my_arr))
print("\n")

#4th way
import copy
z=copy.deepcopy(my_arr)
print(f"The copied array is {z}")
print("Both have different ids",id(z),id(my_arr))
print("\n")


#Reverse
rev_another=my_arr[::-1]
print(f"Array Reversed ---> {rev_another}")
print("\n")


#Sorting
#(Normal sorting)
sorted_arr=sorted(my_arr)
print(f"Array Sorted ---> {sorted_arr}")
print("\n")

#(Reverse sorting)
rev_arr=sorted(my_arr,reverse=True) 
print(f"Array Reverse Sorted ---> {rev_arr}")
print("\n")




#WAP to find the largest number in the array

import array as arr
my_arr=arr.array('i',[5,15,10,30,25,20])
print(f"Created array is ---> {my_arr}")
print("\n")

#1st way
print(f"The greatest value in the array is: {max(my_arr)}")
print("\n")

#2nd way
var=0
for i in my_arr:
    if i>var:
        var=i
print(f"The greatest value in the array is: {var}")
print("\n")

#3rd way
sorted_arr=sorted(my_arr)
print(f"The greatest value in the array is: {sorted_arr[-1]}")
print("\n")

#It can be done in many more ways




#WAP to store all even numbers from one array to another array

import array as arr
#1st way
arr1=arr.array('i',[1,2,3,4,5,6,7])
arr2=arr.array('i')
for i in arr1:
    if i%2==0:
        arr2.append(i)
print(f"The even number array created from an old array is: {arr2}")
print("\n")

#2nd way
arr3=arr.array('i',[i for i in arr1 if i%2==0])
print(f"The even number array created from an old array is: {arr3}")

















