class Solution(object):
    def stoneGameVIII(self, stones):
        """:type stones: List[int]

        :rtype: int
        """
        # Compute prefix sums
        for i in range(1, len(stones)):
            stones[i] += stones[i - 1]

        # The maximum score difference the current player can get
        # starting from the last valid state (prefix sum of all elements)
        res = stones[-1]

        # Iterate backwards from n-2 down to 1
        for i in range(len(stones) - 2, 0, -1):
            res = max(res, stones[i] - res)

        return res
