from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counts = Counter(s)
       
        half_chars = []
        mid_char = ""
        
        for char in sorted(counts.keys()):
            count = counts[char]
            if count % 2 == 1:
                mid_char = char
            half_chars.append(char * (count // 2))
            
        first_half = "".join(half_chars)
        
        return first_half + mid_char + first_half[::-1]
