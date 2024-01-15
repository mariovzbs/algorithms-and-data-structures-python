def selection_sort(arr):
    print("SELECTION SORT", arr)
    n = len(arr)

    for index in range(n):
        for j in range(index, n):
            if arr[j] < arr[index]:
                arr[j], arr[index] = arr[index], arr[j]
    return arr


def main():
    # print("SORT RESULT", selection_sort([5, 3, 4, 1, 2]))
    print("SORT RESULT", selection_sort([64, 34, 25, 12, 22, 11, 90]))


main()
