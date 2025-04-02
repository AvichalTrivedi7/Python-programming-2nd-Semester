# Insertion Sorting

import numpy as np
array1 = list(map(int, input("Enter array elements separated by space: ").split()))
arr1 = np.array(array1)

def insertion_sort(arr):
    # Traverse through the array from the second element to the last
    for i in range(1, len(arr)):
        key = arr[i]  # The current element to be placed in the correct position
        j = i - 1  # Start comparing with the previous elements

        # Move elements that are greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift the element to the right
            j -= 1  # Move to the previous element

        arr[j + 1] = key  # Place the key in its correct position

# Example usage
insertion_sort(arr1)
print("Insertion Sort:", arr1)



# Selection Sorting

def selection_sort(arr):
    n = len(arr)  # Get the length of the array

    # Iterate through all array elements
    for i in range(n):
        min_index = i  # Assume the current index is the minimum

        # Find the smallest element in the remaining unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:  # If a smaller element is found, update min_index
                min_index = j

        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
selection_sort(arr1)
print("Selection Sort:", arr1)