class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        # Count frequencies of remainders modulo 3
        count = [0, 0, 0]
        for stone in stones:
            count[stone % 3] += 1
            
        # Case 1: Even number of 0-remainder stones
        if count[0] % 2 == 0:
            return min(count[1], count[2]) > 0
            
        # Case 2: Odd number of 0-remainder stones
        return abs(count[1] - count[2]) > 2
