def merge_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr

    mid = n // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    i = 0
    j = 0
    n_left = len(left)
    n_right = len(right)
    merged_array = []

    while i < n_left and j < n_right:
        if left[i] <= right[j]:
            merged_array.append(left[i])
            i += 1
        else:
            merged_array.append(right[j])
            j += 1
    merged_array.extend(left[i:])
    merged_array.extend(right[j:])

    return merged_array


arr = [6, 1, 7, 4, 2, 9, 8, 5, 3]
print(merge_sort(arr))
