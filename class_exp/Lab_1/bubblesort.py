def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [1,5,3,8,10,15,24,55,68,103,2,4]
bubblesort(arr)
print(arr)