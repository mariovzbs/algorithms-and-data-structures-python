def binary_search(arr, target):
    return binary_search_recursive(arr, target, 0, len(arr) - 1)


def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, right - 1)


arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
target = 23

result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
