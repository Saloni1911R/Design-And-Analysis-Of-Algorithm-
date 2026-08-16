class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return ""
        
        char_set = set(s)
        
        for i, char in enumerate(s):
            if char.swapcase() not in char_set:
                left_sub = self.longestNiceSubstring(s[:i])
                right_sub = self.longestNiceSubstring(s[i+1:])

                return left_sub if len(left_sub) >= len(right_sub) else right_sub
                
        return s
