def heapify(arr, n, i):
    largest = i                   # Initialize largest as root
    left = 2 * i + 1              # Left child index
    right = 2 * i + 2             # Right child index

    # Check if left child exists and is greater than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # Check if right child exists and is greater than current largest
    if right < n and arr[largest] < arr[right]:
        largest = right

    # If root is not the largest, swap and heapify the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)               # Heapify the root element
    return arr

# Example
print(heap_sort([2, 11, 13, 5, 6, 7]))
