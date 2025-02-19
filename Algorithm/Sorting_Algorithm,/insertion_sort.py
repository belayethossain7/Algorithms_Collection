def insertion_sort(arr):
    for i in range(1, len(arr)):  # Start with the second element
        key = arr[i]  # The element to be placed in the sorted part
        j = i - 1  # Start comparing with the previous element

        # Move elements of arr[0..i-1] that are greater than key
        # one position to the right to make space for the key
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Shift the larger element one position to the right
            j -= 1  # Move to the previous element

        arr[j + 1] = key  # Insert the key at its correct position
    return arr

# Example Usage
sorted_list = insertion_sort([12, 11, 13, 5, 6])
print(sorted_list)  # Output: [5, 6, 11, 12, 13]
