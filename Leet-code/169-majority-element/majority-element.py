class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return nums[0]
        mid = len(nums)//2
        left_majority = self.majorityElement(nums[:mid])
        right_majority = self.majorityElement(nums[mid:])
        if left_majority == right_majority:
            return left_majority

        left_count = nums.count(left_majority)
        right_count = nums.count(right_majority)
        
        return left_majority if left_count > right_count else right_majority