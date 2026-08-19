class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = 0
        n = len(nums)
        
        for i in range(n):
            target_count = 0
            for j in range(i, n):
                if nums[j] == target:
                    target_count += 1
                
                length = j - i + 1
                
                if target_count * 2 > length:
                    ans += 1
                    
        return ans
