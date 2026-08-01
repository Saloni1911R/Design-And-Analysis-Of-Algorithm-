from typing import List
from functools import cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def get_max_diff(i: int, j: int) -> int:
            if i == j:
                return nums[i]
            pick_left = nums[i] - get_max_diff(i + 1, j)
            pick_right = nums[j] - get_max_diff(i, j - 1)          
            return max(pick_left, pick_right)
        return get_max_diff(0, len(nums) - 1) >= 0
