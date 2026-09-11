class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        # dp[i] stores the count of distinct subsequences ending with the letter chr(ord('a') + i)
        dp = [0] * 26
        
        for char in s:
            idx = ord(char) - ord('a')
            # Total distinct subsequences we can form so far plus the single character itself
            total = sum(dp) % MOD
            # New count ending with this character
            dp[idx] = (total + 1) % MOD
            
        return sum(dp) % MOD
