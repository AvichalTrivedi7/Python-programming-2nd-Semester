def merge_sort(arr):
    # Base case: If the array has only one element or is empty, return
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle index to split the array

        left_half = arr[:mid]  # Left half of the array
        right_half = arr[mid:]  # Right half of the array

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves back together
        i = j = k = 0  # Pointers for left_half, right_half, and main array

        # Compare elements and merge them in sorted order
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:  # If left element is smaller
                arr[k] = left_half[i]
                i += 1  # Move the left pointer
            else:
                arr[k] = right_half[j]  # If right element is smaller
                j += 1  # Move the right pointer
            k += 1  # Move the main array pointer

        # Copy any remaining elements from the left half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy any remaining elements from the right half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage
l1 = list(map(int, input("Enter list elements separated by space: ").split()))
merge_sort(l1)
print("Merge Sort:", l1)
