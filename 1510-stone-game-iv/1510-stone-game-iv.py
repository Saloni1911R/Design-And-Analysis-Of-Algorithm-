class Solution(object):
    def winnerSquareGame(self, n):
        # dp[i] represents if the player whose turn it is can win with i stones remaining
        dp = [False] * (n + 1)
        
        # Iterate through all stone states from 1 to n
        for i in range(1, n + 1):
            k = 1
            # Try removing every possible perfect square less than or equal to i
            while k * k <= i:
                # If the remaining stones put the opponent in a losing state, the current player wins
                if not dp[i - k * k]:
                    dp[i] = True
                    break  # Found a winning move, no need to check other squares
                k += 1
                
        return dp[n]
