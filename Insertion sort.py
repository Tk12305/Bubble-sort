def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]           # The element to be inserted
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key       
    return arr


my_list = [9, 5, 1, 4, 3]
sorted_list = insertion_sort(my_list)
print("Sorted list:", sorted_list)


