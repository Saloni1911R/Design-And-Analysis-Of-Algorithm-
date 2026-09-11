class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        
        # Ensure i is the smaller index and j is the larger index
        i = min(min_idx, max_idx)
        j = max(min_idx, max_idx)
        
        # Strategy 1: Remove both from the front (reach index j from the start)
        del_from_front = j + 1
        
        # Strategy 2: Remove both from the back (reach index i from the end)
        del_from_back = n - i
        
        # Strategy 3: Remove one from the front and one from the back
        del_both_sides = (i + 1) + (n - j)
        
        return min(del_from_front, del_from_back, del_both_sides)
