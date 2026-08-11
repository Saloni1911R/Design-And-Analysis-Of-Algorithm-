class Solution(object):
    def missingInteger(self, nums):
        """:type nums: List[int] :rtype: int"""
        pref_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                pref_sum += nums[i]
            else:
                break

        num_set = set(nums)

        current = pref_sum
        while current in num_set:
            current += 1

        return current
