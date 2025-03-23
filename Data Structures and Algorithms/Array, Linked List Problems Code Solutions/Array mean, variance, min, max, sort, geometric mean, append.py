# Array mean, variance, min, max, sort, geometric mean, append.

import array as arr

arr1=arr.array('i',[1,2,3,4,5,6,7,8,9,10])
def variance(a):
     mean = sum(a)/len(a)
     numerator = [(x - mean)**2 for x in a]
     return sum(numerator)/(len(a)-1)

def mean(a):
    return sum(a)/len(a)

def sum_array(a):
    return sum(a)

def min_array(a):
    return min(a)

def max_array(a):
    return max(a)

def sort_array(a):
    return sorted(a,reverse=True)

def GM(a):
    p=1
    for num in a:
        p*=num
    return p**(1/len(a))

def add_element(array,element):
    array.append(element)
    return array
   

print(f"This is the variance of the array --> {variance(arr1)}")
print(f"This is the mean of the array --> {mean(arr1)}")
print(f"This is the sum of the array --> {sum_array(arr1)}")
print(f"This is the min element of the array --> {min_array(arr1)}")
print(f"This is the max element of the array --> {max_array(arr1)}")
print(f"This is the array in reverse sorted order --> {sort_array(arr1)}")
print(f"This is the geometric mean of the array --> {GM(arr1)}")
print(f"This is the array after adding 11 at the last positon --> {add_element(arr1,11)}")


        
