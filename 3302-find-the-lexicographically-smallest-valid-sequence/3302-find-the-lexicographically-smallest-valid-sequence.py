class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        n, m = len(word1), len(word2)
        
        # last[j] stores the maximum index in word1 that can match word2[j:]
        last = [-1] * m
        w1_idx = n - 1
        
        # Precompute valid matches from right to left
        for j in range(m - 1, -1, -1):
            while w1_idx >= 0 and word1[w1_idx] != word2[j]:
                w1_idx -= 1
            if w1_idx >= 0:
                last[j] = w1_idx
                w1_idx -= 1
            else:
                break
                
        ans = []
        w1_idx = 0
        changed = False
        
        # Match greedily from left to right
        for j in range(m):
            # Case 1: Exact character match
            if w1_idx < n and word1[w1_idx] == word2[j]:
                ans.append(w1_idx)
                w1_idx += 1
                continue
                
            # Case 2: Mismatch, try using our single allowed wildcard change
            # FIX: Added 'w1_idx < n' validation to prevent matching non-existent indices
            if not changed and w1_idx < n:
                # We can safely skip/change this character if it's the last character
                # or if the remaining suffix word2[j+1:] can be completely matched ahead.
                if j + 1 == m or (w1_idx + 1 < n and last[j + 1] >= w1_idx + 1):
                    ans.append(w1_idx)
                    w1_idx += 1
                    changed = True
                    continue
                    
            # Case 3: Match cannot be changed here, find the next exact matching character
            while w1_idx < n and word1[w1_idx] != word2[j]:
                w1_idx += 1
                
            if w1_idx < n:
                ans.append(w1_idx)
                w1_idx += 1
            else:
                return []
                
        return ans if len(ans) == m else []
