def minmax(arr):
    # Base case for single element array
    if len(arr) == 1:
        return (arr[0], arr[0])
    
    # Divide and conquer
    mid = len(arr) // 2
    min1, max1 = minmax(arr[:mid])
    min2, max2 = minmax(arr[mid:])

    # Find total minimum
    if min1 < min2:
        final_min = min1
    else:
        final_min = min2

    # Find total maximum
    if max1 > max2:
        final_max = max1
    else:
        final_max = max2

    # CRITICAL FIX: Return the final tuple
    return (final_min, final_max)

arr = [5, 6, 8, 2, 7, 3, 1, 9, 4]
print(minmax(arr))
