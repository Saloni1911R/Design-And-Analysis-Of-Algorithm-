class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        # Start checking numbers from n upwards
        curr = n
        while True:
            # Calculate the product of digits for the current number
            digit_product = 1
            temp = curr
            
            # Extract digits and compute their product
            while temp > 0:
                digit_product *= temp % 10
                temp //= 10
                
            # If the current number is 0, its digit product is 0
            if curr == 0:
                digit_product = 0
                
            # Check if the product is cleanly divisible by t
            if digit_product % t == 0:
                return curr
                
            # Move to the next integer
            curr += 1
