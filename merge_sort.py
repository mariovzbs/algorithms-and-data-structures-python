def merge_sort(arr):
    len_arr = len(arr)
    if len_arr <= 1:
        return arr

    mid = len_arr // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    len_left = len(left)
    len_right = len(right)
    while i < len_left and j < len_right:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def main():
    print("SORT RESULT", merge_sort([5, 3, 4, 1, 2]))
    print("SORT RESULT", merge_sort([12, 11, 13, 5, 6, 7]))


main()
