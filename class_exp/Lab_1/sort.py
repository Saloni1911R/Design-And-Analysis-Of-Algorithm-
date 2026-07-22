def sort_array(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr
arr = [1,5,3,8,10,15,24,55,68,103,2,4]
sort_array(arr)
print(arr)