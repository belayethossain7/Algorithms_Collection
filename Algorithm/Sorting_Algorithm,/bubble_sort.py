def bubble_sort(arr):
    
    n = len(arr)  # Get the length of the list
    # Outer loop: Number of passes through the list
    for i in range(n - 1):  # We need (n-1) passes
        swapped = False  # To optimize, track if a swap is made
        print(f"Pass {i+1}:")  # Debug: Show pass number
        # Inner loop: Compare adjacent elements
        for j in range(n - i - 1):  # Each pass excludes the sorted elements
            print(f"  Comparing {arr[j]} and {arr[j + 1]}")  # Debug
            if arr[j] > arr[j + 1]:  # Swap if elements are out of order
                print(f"  Swapping {arr[j]} and {arr[j + 1]}")  # Debug
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # A swap occurred
        print(f"  List after pass {i+1}: {arr}")  # Debug: Show list state
        if not swapped:  # If no swaps, list is sorted
            print("No swaps made, list is sorted!")
            break  # Optimization to stop early
    return arr

# Example Usage
unsorted_list = [5, 1, 4, 2, 8]
print("Unsorted List:", unsorted_list)
sorted_list = bubble_sort(unsorted_list)
print("Sorted List:", sorted_list)
