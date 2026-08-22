class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Initialize arrays with the first two elements
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        
        # Loop through the remaining elements
        for i in range(2, len(nums)):
            # Compare the last elements of both arrays
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
                
        # Concatenate and return the final combined array
        return arr1 + arr2
