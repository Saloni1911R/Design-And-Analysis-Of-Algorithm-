from collections import Counter

class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n = len(s)
        count = Counter(s)
        
        # 1. Validate if a palindrome can be formed
        odd_chars = [char for char, cnt in count.items() if cnt % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        mid = odd_chars[0] if odd_chars else ""
        half_counts = {char: cnt // 2 for char, cnt in count.items()}
        half_len = n // 2
        
        def make_palindrome(h):
            return h + mid + h[::-1]
            
        # 2. Check if the absolute smallest palindrome possible is already > target
        smallest_half = []
        for char in sorted(half_counts.keys()):
            smallest_half.append(char * half_counts[char])
        smallest_palindrome = make_palindrome("".join(smallest_half))
        
        if smallest_palindrome > target:
            return smallest_palindrome
            
        # 3. Greedy Approach: Try to match target's prefix up to index i, 
        # then make index i strictly greater than target[i].
        best_palindrome = None
        
        # Case A: First half matches target[:half_len] exactly
        can_match_exact = True
        rem_counts = half_counts.copy()
        for c in target[:half_len]:
            if rem_counts.get(c, 0) > 0:
                rem_counts[c] -= 1
            else:
                can_match_exact = False
                break
                
        if can_match_exact:
            exact_palindrome = make_palindrome(target[:half_len])
            if exact_palindrome > target:
                best_palindrome = exact_palindrome

        # Case B: Match target up to index i-1, and make character at index i larger
        for i in range(half_len - 1, -1, -1):
            rem_counts = half_counts.copy()
            possible = True
            
            # Match the prefix target[:i]
            for c in target[:i]:
                if rem_counts.get(c, 0) > 0:
                    rem_counts[c] -= 1
                else:
                    possible = False
                    break
            if not possible:
                continue
                
            # Try to pick a character for position i that is strictly greater than target[i]
            for c in sorted(rem_counts.keys()):
                if c > target[i] and rem_counts[c] > 0:
                    curr_half = list(target[:i]) + [c]
                    rem_counts_copy = rem_counts.copy()
                    rem_counts_copy[c] -= 1
                    
                    # Fill the remaining slots greedily with the smallest available characters
                    for rc in sorted(rem_counts_copy.keys()):
                        curr_half.append(rc * rem_counts_copy[rc])
                    
                    candidate = make_palindrome("".join(curr_half))
                    if candidate > target:
                        if best_palindrome is None or candidate < best_palindrome:
                            best_palindrome = candidate
                    break # Smallest valid character chosen for position i, move to next prefix length
                    
        return best_palindrome if best_palindrome is not None else ""
