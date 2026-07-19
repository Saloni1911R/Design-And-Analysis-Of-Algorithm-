def selectionsort(arr):
    n = len(arr)
    for i in range(0,n):
        min_index = i
        for j in range(i,n):
            if (arr[j] <arr[min_index]):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [1,5,3,8,10,15,24,55,68,103,2,4]
selectionsort(arr)
print(arr)