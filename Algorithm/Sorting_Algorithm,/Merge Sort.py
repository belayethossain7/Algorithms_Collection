def merge_sort(arr):
    # Base case: If the array has one or no elements, it is already sorted.
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_sort = arr[:mid]
    right_sort = arr[mid:]
    
    # Recursive calls to sort each half
    left_sort = merge_sort(left_sort)
    right_sort = merge_sort(right_sort)
    
    # Merge the sorted halves
    i = j = k = 0
    while i < len(left_sort) and j < len(right_sort):
        if left_sort[i] < right_sort[j]:
            arr[k] = left_sort[i]
            i += 1
        else:
            arr[k] = right_sort[j]
            j += 1
        k += 1
    
    # Add any remaining elements from left_sort
    while i < len(left_sort):
        arr[k] = left_sort[i]
        i += 1
        k += 1
    
    # Add any remaining elements from right_sort
    while j < len(right_sort):
        arr[k] = right_sort[j]
        j += 1
        k += 1
    
    return arr

# Call function
print(merge_sort([5, 2, 4, 7, 1, 3, 2, 6]))
