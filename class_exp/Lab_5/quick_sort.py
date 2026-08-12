def partition(arr,start,end):
    pivot = arr[end]
    pIndex = start
    for i in range(start,end):
        if(arr[i] <= pivot):
            arr[i],arr[pIndex] = arr[pIndex],arr[i]
            pIndex += 1
    arr[pIndex],arr[end] = arr[end],arr[pIndex]
    return pIndex

def quick_sort(arr,start,end):
    if(start<end):
        pIndex = partition(arr,start,end)
        quick_sort(arr,start,pIndex-1) # left side of pivot
        quick_sort(arr,pIndex+1,end) # right side of pivot
        return arr


arr = [5, 6, 8, 2, 7, 3, 1, 9, 4]
print(quick_sort(arr,0,len(arr)-1))