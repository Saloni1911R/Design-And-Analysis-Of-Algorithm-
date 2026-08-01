from typing import List
from functools import cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def get_max_diff(i: int, j: int) -> int:
            # Base case: only one element left
            if i == j:
                return nums[i]
            
            # Option 1: Pick the left element
            pick_left = nums[i] - get_max_diff(i + 1, j)
            # Option 2: Pick the right element
            pick_right = nums[j] - get_max_diff(i, j - 1)
            
            # Return the maximum score difference the current player can secure
            return max(pick_left, pick_right)
        
        # If Player 1's score minus Player 2's score is >= 0, Player 1 wins or ties
        return get_max_diff(0, len(nums) - 1) >= 0
