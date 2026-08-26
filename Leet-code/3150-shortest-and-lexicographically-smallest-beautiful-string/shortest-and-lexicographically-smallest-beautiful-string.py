class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Collect all indices where character is '1'
        ones_indices = [i for i, char in enumerate(s) if char == '1']
        
        # If there are fewer than k '1's, no beautiful substring exists
        if len(ones_indices) < k:
            return ""
            
        res = ""
        min_len = float('inf')
        
        # Check every window containing exactly k '1's
        for i in range(len(ones_indices) - k + 1):
            start = ones_indices[i]
            end = ones_indices[i + k - 1]
            
            # Extract the substring
            substring = s[start:end + 1]
            current_len = len(substring)
            
            # Update if it's shorter, or same length but lexicographically smaller
            if current_len < min_len:
                min_len = current_len
                res = substring
            elif current_len == min_len:
                if substring < res:
                    res = substring
                    
        return res
