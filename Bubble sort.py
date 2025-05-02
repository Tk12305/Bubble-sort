def bubble_sort(arr):  # Function to perform bubble sort
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Example usage
my_list = [2, 3, 8, 5, 2]
sorted_list = bubble_sort(my_list)
print("Sorted list:", sorted_list)

