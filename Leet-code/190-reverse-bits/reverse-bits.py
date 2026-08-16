class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        
        for _ in range(32):
            # Shift result to the left for the next bit
            result <<= 1
            
            # Extract the rightmost bit of n and add it to result
            result |= (n & 1)
            
            # Shift n to the right to process the next bit
            n >>= 1
            
        return result
