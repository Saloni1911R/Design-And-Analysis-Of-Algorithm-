class SparseTable:
    def __init__(self, nums):
        self.n = len(nums)
        if self.n == 0:
            self.st = []
            return
        
        # st[i][j] := max(nums[j .. j + 2^i - 1])
        levels = self.n.bit_length()
        self.st = [[0] * self.n for _ in range(levels)]
        self.st[0] = list(nums)  # Replaced .copy() with list(nums)
        
        for i in range(1, levels):
            length = 1 << (i - 1)
            for j in range(self.n - (1 << i) + 1):
                self.st[i][j] = max(
                    self.st[i - 1][j],
                    self.st[i - 1][j + length]
                )

    def query(self, l, r):
        """Returns max(nums[l..r])."""
        if not self.st or l > r:
            return 0
        i = (r - l + 1).bit_length() - 1
        return max(self.st[i][l], self.st[i][r - (1 << i) + 1])


class Solution:
    def maxActiveSectionsAfterTrade(self, s, queries):
        n = len(s)
        ones = s.count('1')
        
        # Identify zero groups and map each index to its group index
        zero_groups = []  # Stores [start_index, length]
        zero_group_index = []
        
        for i in range(n):
            if s[i] == '0':
                if i > 0 and s[i - 1] == '0':
                    zero_groups[-1][1] += 1
                else:
                    zero_groups.append([i, 1])
            zero_group_index.append(len(zero_groups) - 1)
            
        if not zero_groups:
            return [ones] * len(queries)

        # Merge lengths of adjacent groups
        zero_merge_lengths = [
            zero_groups[i][1] + zero_groups[i + 1][1] 
            for i in range(len(zero_groups) - 1)
        ]
        
        st = SparseTable(zero_merge_lengths)

        res = []
        for l, r in queries:
            l_idx = zero_group_index[l]
            left = -1 if l_idx == -1 else zero_groups[l_idx][1] - (l - zero_groups[l_idx][0])

            r_idx = zero_group_index[r]
            right = -1 if r_idx == -1 else r - zero_groups[r_idx][0] + 1

            start_adj_idx = l_idx + 1
            end_adj_idx = r_idx if s[r] == '1' else r_idx - 1
            
            range_l = start_adj_idx
            range_r = end_adj_idx - 1

            active_sections = ones
            
            if s[l] == '0' and s[r] == '0' and l_idx + 1 == r_idx:
                active_sections = max(active_sections, ones + left + right)
            elif range_l <= range_r:
                active_sections = max(
                    active_sections,
                    ones + st.query(range_l, range_r)
                )

            if s[l] == '0' and l_idx + 1 <= (r_idx if s[r] == '1' else r_idx - 1):
                active_sections = max(
                    active_sections,
                    ones + left + zero_groups[l_idx + 1][1]
                )

            if s[r] == '0' and l_idx < r_idx - 1:
                active_sections = max(
                    active_sections,
                    ones + right + zero_groups[r_idx - 1][1]
                )

            res.append(active_sections)

        return res