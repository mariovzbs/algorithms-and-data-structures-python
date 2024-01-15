def quick_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr

    pivot = arr[n // 2]
    left, middle, right = partition(pivot, arr)
    return quick_sort(left) + middle + quick_sort(right)


def partition(pivot, arr):
    left = []
    middle = []
    right = []

    for value in arr:
        if value < pivot:
            left.append(value)
        elif value > pivot:
            right.append(value)
        else:
            middle.append(value)

    return left, middle, right


arr = [6, 1, 7, 4, 2, 9, 8, 5, 3]
print(quick_sort(arr))
