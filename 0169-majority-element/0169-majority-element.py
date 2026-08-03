class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0
        
        for num in nums:
            # If count drops to 0, pick the current number as the new candidate
            if count == 0:
                candidate = num
            
            # Increment count if num matches candidate, otherwise decrement
            count += 1 if num == candidate else -1
            
        return candidate
