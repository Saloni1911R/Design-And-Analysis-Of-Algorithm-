class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        n = len(stoneValue)
        if n == 1:
            return 0
            
        # Prefix sum array
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]
            
        # dp[i][j]: max score for subarray stoneValue[i...j]
        dp = [[0] * n for _ in range(n)]
        
        # max_left[i][j] = max(dp[i][k] + sum(i, k)) for k from i to j
        max_left = [[0] * n for _ in range(n)]
        # max_right[i][j] = max(dp[k][j] + sum(k, j)) for k from i to j
        max_right = [[0] * n for _ in range(n)]
        
        # Base cases for single elements
        for i in range(n):
            max_left[i][i] = stoneValue[i]
            max_right[i][i] = stoneValue[i]
            
        # Outer loops for range DP
        for length in range(2, n + 1):
            mid = 0  # Monotonic pointer tracking split point where left_sum <= right_sum
            for i in range(n - length + 1):
                j = i + length - 1
                
                # Advance mid pointer while left part is smaller than or equal to right part
                # Total sum of interval = pref[j+1] - pref[i]
                # Left part sum = pref[mid+1] - pref[i]
                while (pref[mid + 1] - pref[i]) * 2 <= (pref[j + 1] - pref[i]):
                    mid += 1
                
                max_score = 0
                
                # Case 1: Split point is <= mid - 1
                # Here left_sum < right_sum, Bob drops the right side.
                # We need max(dp[i][k] + left_sum), which is cached in max_left[i][mid-1]
                if i <= mid - 1:
                    max_score = max(max_score, max_left[i][mid - 1])
                    
                # Case 2: Split point is >= mid + 1
                # Here left_sum > right_sum, Bob drops the left side.
                # We need max(dp[k+1][j] + right_sum), which is cached in max_right[mid+1][j]
                if mid + 1 <= j:
                    max_score = max(max_score, max_right[mid + 1][j])
                    
                # Case 3: Edge case where left_sum == right_sum exactly
                # This only happens if mid points to an exact half-split
                if (pref[mid] - pref[i]) * 2 == (pref[j + 1] - pref[i]):
                    max_score = max(max_score, max_left[i][mid - 1])
                    max_score = max(max_score, max_right[mid][j])
                
                dp[i][j] = max_score
                
                # Maintain the auxiliary optimization tables for subsequent ranges
                total_range_sum = pref[j + 1] - pref[i]
                max_left[i][j] = max(max_left[i][j - 1], dp[i][j] + total_range_sum)
                max_right[i][j] = max(max_right[i + 1][j], dp[i][j] + total_range_sum)
                
        return dp[0][n - 1]
