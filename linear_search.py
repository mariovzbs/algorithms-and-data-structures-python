def linear_search(arr, value):
    for item in arr:
        if value == item:
            return True
    return False


arr = [64, 34, 25, 12, 22, 11, 90]
print(linear_search(arr, 90))
print(linear_search(arr, 23))
