class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Base case: strings shorter than 2 characters cannot be nice
        if len(s) < 2:
            return ""
        
        char_set = set(s)
        
        for i, char in enumerate(s):
            # If the matching case (upper or lower) is missing, split here
            if char.swapcase() not in char_set:
                # Recursively check the left and right substrings
                left_sub = self.longestNiceSubstring(s[:i])
                right_sub = self.longestNiceSubstring(s[i+1:])
                
                # Return the longer of the two substrings
                # Use >= or len comparison to ensure the earliest one is picked on tie
                return left_sub if len(left_sub) >= len(right_sub) else right_sub
                
        return s
