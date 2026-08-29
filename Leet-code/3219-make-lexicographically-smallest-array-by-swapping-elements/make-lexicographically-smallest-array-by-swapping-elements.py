class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        n = len(nums)
        # Pair each value with its original index
        indexed_nums = sorted([(nums[i], i) for i in range(n)])
        
        res = [0] * n
        i = 0
        while i < n:
            j = i
            # Find the group of numbers where adjacent difference <= limit
            while j < n - 1 and indexed_nums[j + 1][0] - indexed_nums[j][0] <= limit:
                j += 1
                
            # Extract values and original indices for this group
            group_vals = [indexed_nums[k][0] for k in range(i, j + 1)]
            group_indices = sorted([indexed_nums[k][1] for k in range(i, j + 1)])
            
            # Place sorted values into sorted original positions
            for idx, val in zip(group_indices, group_vals):
                res[idx] = val
                
            i = j + 1
            
        return res
