class Solution(object):
    def maxNumOfSubstrings(self, s):
        left_pos = {c: s.find(c) for c in set(s)}
        right_pos = {c: s.rfind(c) for c in set(s)}
        
        def get_valid_interval(i):
            right = right_pos[s[i]]
            j = i
            while j <= right:
                c = s[j]
                if left_pos[c] < i:
                    return -1
                right = max(right, right_pos[c])
                j += 1
            return right

        intervals = []
        for i in range(len(s)):
            if i == left_pos[s[i]]:
                r = get_valid_interval(i)
                if r != -1:
                    intervals.append([i, r])
        
        # Sort by end position
        intervals.sort(key=lambda x: x[1])
        
        res = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                res.append(s[start:end+1])
                prev_end = end
                
        return res
