class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digits = [int(d) for d in str(n)]
        
        # Calculate sum
        digit_sum = sum(digits)
        
        # Calculate product
        digit_prod = 1
        for d in digits:
            digit_prod *= d
            
        combined = digit_sum + digit_prod
        
        # Check if n is completely divisible by the combined sum + product
        return n % combined == 0
