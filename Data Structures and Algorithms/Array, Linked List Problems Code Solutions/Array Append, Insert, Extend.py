
import array as arr
arr1=arr.array("i",[1,2,3,5,6,7])
arr2=arr.array("i",[9,10])
arr1.append(8)
arr1.insert(0,0)
arr1.extend(arr2)
print(arr1)
