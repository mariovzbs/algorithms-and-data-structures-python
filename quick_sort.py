def quick_sort(arr):
    len_arr = len(arr)
    if len_arr <= 1:
        return arr
    pivot = arr[len_arr // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def main():
    print("SORT RESULT", quick_sort([5, 3, 4, 1, 2]))
    print("SORT RESULT", quick_sort([12, 11, 13, 5, 6, 7]))


main()
