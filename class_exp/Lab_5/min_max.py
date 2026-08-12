def minmax(arr,start,end):
    if(start == end):
        return (arr[start],arr[start])
    if(end == start + 1):
        if(arr[start] < arr[end]):
            return (arr[start],arr[end])
        else:
            return (arr[end],arr[start])
    mid = (start + end)//2
    min1,max1 = minmax(arr,start,mid)
    min2,max2 = minmax(arr,mid+1,end)
    if(min1 < min2):
        min_f = min1
    else:
        min_f = min2
    if(max1 > max2):
        max_f = max1
    else:
        max_f = max2
    return (min_f,max_f)

x = [1,2,3,4,5,66,7,8,9]
print(minmax(x,0,len(x)-1))