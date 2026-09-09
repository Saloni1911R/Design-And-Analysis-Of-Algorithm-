class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        x = 1000
        while x <= n:
            ans += n - x + 1
            x *= 1000
        return ans