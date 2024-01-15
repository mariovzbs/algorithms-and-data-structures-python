def insertion_sort(arr):
    n = len(arr)

    for index in range(1, n):
        temp = arr[index]
        j = index - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

    return arr


arr = [6, 1, 7, 4, 2, 9, 8, 5, 3]
print(insertion_sort(arr))
