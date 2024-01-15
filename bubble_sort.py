def while_bubble_sort(arr):
    print("WHILE BUBBLE SORT", arr)
    index = 0
    arr_length = len(arr)

    while index < arr_length:
        if index + 1 == arr_length:
            break
        elif arr[index] > arr[index + 1]:
            temp = arr[index + 1]
            arr[index + 1] = arr[index]
            arr[index] = temp
            index = 0
        else:
            index += 1
        print("SORTING", index, arr)

    return arr


def bubble_sort(arr):
    print("BUBBLE SORT", arr)
    n = len(arr)
    for index in range(n):
        for j in range(0, n - index - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print("SORTING", arr)
    return arr


def main():
    print("SORT RESULT", bubble_sort([5, 3, 4, 1, 2]))
    print("SORT RESULT", bubble_sort([64, 34, 25, 12, 22, 11, 90]))
    # print("SORT RESULT", while_bubble_sort([5, 3, 4, 1, 2]))


main()
