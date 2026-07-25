class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = sorted([int(d) for d in str(n)], reverse=True)
        return digits[0] * digits[1]
