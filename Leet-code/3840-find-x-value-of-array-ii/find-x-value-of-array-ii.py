class SegmentTree:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k
        # Each node stores: (total_product_mod_k, counts_array_of_size_k)
        self.tree = [None] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)

    def _merge(self, left, right):
        if not left: return right
        if not right: return left
        
        lp, lc = left
        rp, rc = right
        
        # New total product
        np = (lp * rp) % self.k
        
        # New counts
        nc = list(lc) # Start with left child counts
        for r in range(self.k):
            if rc[r] > 0:
                next_rem = (lp * r) % self.k
                nc[next_rem] += rc[r]
                
        return (np, nc)

    def build(self, nums, node, start, end):
        if start == end:
            rem = nums[start] % self.k
            counts = [0] * self.k
            counts[rem] = 1
            self.tree[node] = (rem, counts)
            return

        mid = (start + end) // 2
        self.build(nums, 2 * node + 1, start, mid)
        self.build(nums, 2 * node + 2, mid + 1, end)
        self.tree[node] = self._merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def update(self, node, start, end, idx, val):
        if start == end:
            rem = val % self.k
            counts = [0] * self.k
            counts[rem] = 1
            self.tree[node] = (rem, counts)
            return

        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node + 1, start, mid, idx, val)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, val)
        self.tree[node] = self._merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return None
        if l <= start and end <= r:
            return self.tree[node]

        mid = (start + end) // 2
        left_res = self.query(2 * node + 1, start, mid, l, r)
        right_res = self.query(2 * node + 2, mid + 1, end, l, r)
        return self._merge(left_res, right_res)


class Solution(object):
    def resultArray(self, nums, k, queries):
        """
        :type nums: List[int]
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        st = SegmentTree(nums, k)
        result = []
        
        for idx, val, start, x in queries:
            # 1. Update the value at the given index
            st.update(0, 0, n - 1, idx, val)
            
            # 2. Query the range from start to the end of the array
            res = st.query(0, 0, n - 1, start, n - 1)
            
            # 3. Extract the counts array and append the target x-value count
            if res:
                result.append(res[1][x])
            else:
                result.append(0)
                
        return result
