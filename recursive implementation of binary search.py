def binary_search(arr, init, end, find):
    if end >= init:
        mid = (init + end) // 2
        if arr[mid] == find:
            print(mid)
        elif arr[mid] > find:
            end = mid - 1
            binary_search(arr, init, end, find)
        elif arr[mid] < find:
            init = mid + 1
            binary_search(arr, init, end, find)
    else:
        print("Number not found")


arr = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11]
init = 0
end = len(arr)-1
find = 11
binary_search(arr, init, end, find)
