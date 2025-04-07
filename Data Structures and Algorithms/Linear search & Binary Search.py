# Linear Search

import numpy as np
array1 = list(map(int, input("Enter array elements separated by space: ").split()))
elei = int(input("Enter the element to search: "))
arr1 = np.array(array1)

def linearSearch(a, ele):
    flag=0
    for i in range(len(a)):
        if a[i]==ele:
            print(f"Element {ele} found at index {i}")
            flag+=1
            return
        
    if flag==0:
        print("Element not found")


linearSearch(arr1, elei)


#Binary Search

def binarySearch1(a,ele):
    print("First we sort and then for the binary search, --->")
    binarySearch(sorted(a),ele)
            
def binarySearch(a, ele):
    print(f"This is the array {a}")
    
    leng=len(a)
    if a[leng//2]==ele:
        print(f"Element {ele} found.")
        return
    
    if leng==1 and a[0]!=ele:
        print("Element not found")
        return
    
    else:
        if ele > a[(leng//2)]:
            leng=leng//2
            binarySearch(a[leng+1:],ele)

        else:
            leng=leng//2
            binarySearch(a[:leng-1],ele)


binarySearch1(arr1,elei)
