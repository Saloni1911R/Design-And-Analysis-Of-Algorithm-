class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = {}
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            num = nums[right]
            freq[num] = freq.get(num, 0) + 1
            
            while freq[num] > k:
                left_num = nums[left]
                freq[left_num] -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        return max_len
