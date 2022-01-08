def binary_search(arr, init, end, find):
    while end >= init:
        mid = (init + end) // 2
        if arr[mid] == find:
            return mid
        elif arr[mid] > find:
            end = mid - 1
        elif arr[mid] < find:
            init = mid + 1
    else:
        return "Number not found"


arr = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11]
init = 0
end = len(arr)-1
find = 12
print(binary_search(arr, init, end, find))
