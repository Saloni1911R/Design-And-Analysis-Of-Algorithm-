class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_set = set(nums)
        min_val = min(nums)
        max_val = max(nums)
        
        missing = []
        for x in range(min_val + 1, max_val):
            if x not in num_set:
                missing.append(x)
                
        return missing
