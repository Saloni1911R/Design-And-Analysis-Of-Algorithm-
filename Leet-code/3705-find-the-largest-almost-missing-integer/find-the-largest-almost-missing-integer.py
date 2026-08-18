class Solution(object):
    def largestInteger(self, nums, k):
        """:type nums: List[int]

        :type k: int
        :rtype: int
        """
        n = len(nums)
        if k == n:
            return max(nums)

        counts = {}
        for x in nums:
            counts[x] = counts.get(x, 0) + 1

        if k == 1:
            ans = -1
            for x in counts:
                if counts[x] == 1:
                    ans = max(ans, x)
            return ans

        ans = -1
        # Check first element
        if counts[nums[0]] == 1:
            ans = max(ans, nums[0])
        # Check last element
        if counts[nums[-1]] == 1:
            ans = max(ans, nums[-1])

        return ans
