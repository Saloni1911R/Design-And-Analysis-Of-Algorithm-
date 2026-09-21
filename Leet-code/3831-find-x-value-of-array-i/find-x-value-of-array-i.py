class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = [0] * k
        # dp[x] stores the number of valid prefixes ending just before the current element
        # that result in a product modulo k equal to x when multiplied forward.
        # Alternatively, dp[x] is the number of subarrays ending at the current index with product % k == x.
        dp = [0] * k
        
        for num in nums:
            rem = num % k
            next_dp = [0] * k
            
            # Start a new subarray at the current element
            next_dp[rem] += 1
            
            # Extend existing subarrays ending at the previous element
            for x in range(k):
                if dp[x] > 0:
                    next_dp[(x * rem) % k] += dp[x]
            
            # Accumulate the counts for all subarrays ending at this element
            for x in range(k):
                ans[x] += next_dp[x]
                
            dp = next_dp
            
        return ans
