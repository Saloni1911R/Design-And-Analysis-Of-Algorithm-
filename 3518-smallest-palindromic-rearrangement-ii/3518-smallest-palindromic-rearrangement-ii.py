from collections import Counter
import math

class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        count = Counter(s)
        
        # Find the middle character for odd-length palindromes
        mid_char = ""
        for c, freq in count.items():
            if freq % 2 != 0:
                mid_char = c
                break
        
        # Extract the characters that make up the first half
        half_freq = {c: freq // 2 for c, freq in count.items() if freq // 2 > 0}
        half_len = sum(half_freq.values())
        
        # Initial calculation of total permutations using the multinomial formula
        def get_initial_permutations(freq_map):
            total_slots = sum(freq_map.values())
            if total_slots == 0:
                return 1
            ans = math.factorial(total_slots)
            for f in freq_map.values():
                ans //= math.factorial(f)
            return ans

        total_perms = get_initial_permutations(half_freq)
        if k > total_perms:
            return ""
            
        result_half = []
        # Optimization: track alphabet indices for fast lookups
        sorted_chars = sorted(half_freq.keys())
        
        # Construct the first half sequentially
        N = half_len
        for _ in range(half_len):
            for c in sorted_chars:
                if half_freq[c] > 0:
                    # O(1) mathematical reduction to check permutations if we pick 'c'
                    possible_perms = (total_perms * half_freq[c]) // N
                    
                    if k <= possible_perms:
                        # Character 'c' is correct; accept the transition
                        result_half.append(c)
                        half_freq[c] -= 1
                        total_perms = possible_perms
                        N -= 1
                        break
                    else:
                        # Skip this block of permutations and adjust k
                        k -= possible_perms
                        
        first_half = "".join(result_half)
        return first_half + mid_char + first_half[::-1]
