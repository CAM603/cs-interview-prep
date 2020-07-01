def rotated_search(arr, target):
    # bad array
    if not arr:
        return -1

    left = 0
    right = len(arr) - 1

    # stops when we find smallest element
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid

    start = left
    left = 0
    right = len(arr) - 1

    if target >= arr[start] and target <= arr[right]:
        left = start
    else:
        right = start

    # binary search
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return - 1


print(rotated_search([4, 5, 1, 2, 3], 3))
