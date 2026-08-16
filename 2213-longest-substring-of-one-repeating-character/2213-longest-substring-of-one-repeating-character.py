class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)
        # Using parallel arrays instead of objects to completely eliminate object overhead
        left_len = [0] * (4 * n)
        right_len = [0] * (4 * n)
        max_len = [0] * (4 * n)
        pref_char = [""] * (4 * n)
        suff_char = [""] * (4 * n)
        total_len = [0] * (4 * n)
        
        def merge(node):
            left = 2 * node
            right = 2 * node + 1
            
            t_len_l = total_len[left]
            t_len_r = total_len[right]
            
            total_len[node] = t_len_l + t_len_r
            pref_char[node] = pref_char[left]
            suff_char[node] = suff_char[right]
            
            l_len = left_len[left]
            if l_len == t_len_l and pref_char[left] == pref_char[right]:
                l_len += left_len[right]
            left_len[node] = l_len
                
            r_len = right_len[right]
            if r_len == t_len_r and suff_char[right] == suff_char[left]:
                r_len += right_len[left]
            right_len[node] = r_len
                
            m_len = max_len[left] if max_len[left] > max_len[right] else max_len[right]
            if suff_char[left] == pref_char[right]:
                combined = right_len[left] + left_len[right]
                if combined > m_len:
                    m_len = combined
            max_len[node] = m_len

        def build(node, start, end):
            if start == end:
                left_len[node] = 1
                right_len[node] = 1
                max_len[node] = 1
                total_len[node] = 1
                pref_char[node] = s[start]
                suff_char[node] = s[start]
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            merge(node)

        def update(node, start, end, idx, char):
            if start == end:
                pref_char[node] = char
                suff_char[node] = char
                return
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node, start, mid, idx, char)
            else:
                update(2 * node + 1, mid + 1, end, idx, char)
            merge(node)

        build(1, 0, n - 1)
        ans = []
        s_list = list(s)
        
        for ch, idx in zip(queryCharacters, queryIndices):
            if s_list[idx] != ch:
                s_list[idx] = ch
                update(1, 0, n - 1, idx, ch)
            ans.append(max_len[1])
            
        return ans
