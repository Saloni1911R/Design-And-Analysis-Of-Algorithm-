def binary_search(arr, key, low, high):
    if low > high:
        return -1  
        
    mid = (low + high) // 2
    
    if arr[mid] == key:
        return mid
    elif key > arr[mid]:
        # Search the right half: update low boundary
        return binary_search(arr, key, mid + 1, high)
    else:
        # Search the left half: update high boundary
        return binary_search(arr, key, low, mid - 1)

# Main execution logic
arr = [1, 2, 3, 4, 5, 8, 10, 15, 24, 55, 68, 103]
key = 24

# Fixed the argument alignment to match the function definition
result = binary_search(arr, key, 0, len(arr) - 1)

# Fixed the syntax typo in the string conditional check
if result != -1:
    print(f"Element found at index: {result}")
    # Output: Element found at index: 8
else:
    print("Element not found in the array.")
