class Solution(object):
    def stoneGameII(self, piles):
        n = len(piles)
        # Suffix sums to get remaining stones quickly
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        memo = {}
        
        def dp(i, M):
            if i >= n:
                return 0
            if i + 2 * M >= n:
                return suffix_sum[i]
            if (i, M) in memo:
                return memo[(i, M)]
            
            res = 0
            # Try all possible choices X from 1 to 2M
            for X in range(1, 2 * M + 1):
                # Maximize current stones minus what opponent gets in their next turn
                res = max(res, suffix_sum[i] - dp(i + X, max(M, X)))
                
            memo[(i, M)] = res
            return res
            
        return dp(0, 1)
