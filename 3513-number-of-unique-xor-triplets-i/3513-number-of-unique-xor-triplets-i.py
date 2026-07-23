class Solution(object):
    def uniqueXorTriplets(self, nums):
        """:type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Base edge cases where the full bitmask span is not reachable
        if n == 1:
            return 1
        if n == 2:
            return 2
            
        # For n >= 3, find the next power of 2
        ans = 1
        while ans <= n:
            ans <<= 1
        return ans
