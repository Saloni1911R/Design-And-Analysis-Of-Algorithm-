class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        import re
        
        # Count the baseline number of 1s in the original string
        total_ones = s.count('1')
        
        # Group adjacent identical characters into blocks (e.g., ['0', '1', '00'])
        blocks = re.findall(r'0+|1+', s)
        block_list = [(b[0], len(b)) for b in blocks]
        
        max_gain = 0
        
        # Iterate through the blocks, looking for an internal '1'-block
        # It must be strictly bounded by '0'-blocks on both its left and right
        for i in range(1, len(block_list) - 1):
            if (block_list[i][0] == '1' and 
                block_list[i-1][0] == '0' and 
                block_list[i+1][0] == '0'):
                
                # The net gain is the total number of adjacent zeros flipped to ones
                gain = block_list[i-1][1] + block_list[i+1][1]
                if gain > max_gain:
                    max_gain = gain
                    
        return total_ones + max_gain
