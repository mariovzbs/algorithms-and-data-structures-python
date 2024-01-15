def insertion_sort(arr):
    print("INSERTION SORT", arr)
    n = len(arr)

    for index in range(1, n):
        value = arr[index]
        j = index - 1
        while j >= 0 and value < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Here I add 1 because I have already substracted 1 from j hence not being in the position I thought I was.
        arr[j + 1] = value
    return arr


def main():
    print("SORT RESULT", insertion_sort([5, 3, 4, 1, 2]))
    print("SORT RESULT", insertion_sort([64, 34, 25, 12, 22, 11, 90]))


main()
