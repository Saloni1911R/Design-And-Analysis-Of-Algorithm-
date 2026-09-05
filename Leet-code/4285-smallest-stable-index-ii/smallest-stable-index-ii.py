class Solution(object):
    def firstStableIndex(self, nums, k):
        """:type nums: List[int] :type k: int :rtype: int"""
        n = len(nums)
        right = [0] * n
        right[n - 1] = nums[n - 1]
        
        # Precompute minimum values from right to left
        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i])
            
        left = 0
        # Iterate from left to right and track max value
        for i in range(n):
            left = max(left, nums[i])
            if left - right[i] <= k:
                return i
                
        return -1
