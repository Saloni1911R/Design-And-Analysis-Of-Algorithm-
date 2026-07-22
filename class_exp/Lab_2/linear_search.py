def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

arr = [1,2,3,4,5,8,10,15,24,55,68,103,2,4]
key = 99
result = linear_search(arr, key)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array.")