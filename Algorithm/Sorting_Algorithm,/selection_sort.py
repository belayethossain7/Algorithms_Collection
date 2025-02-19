def selection_sort(arr):
    n = len(arr)  # Number of elements in the list
    for i in range(n):  # Loop through the list
        min_idx = i  # Assume the current index is the smallest
        for j in range(i + 1, n):  # Look for a smaller element in the unsorted part
            if arr[j] < arr[min_idx]:  # Update the index if a smaller element is found
                min_idx = j
        # Swap the smallest element with the element at the current position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example Usage
sorted_list = selection_sort([64, 25, 12, 22, 11])
print(sorted_list)  # Output: [11, 12, 22, 25, 64]
