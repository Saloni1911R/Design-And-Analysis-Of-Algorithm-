class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # Unpack the coordinates
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        
        # Check if one is to the left, right, above, or below the other
        is_left = x2 <= x3
        is_right = x1 >= x4
        is_below = y2 <= y3
        is_above = y1 >= y4
        
        # If any of these non-overlapping conditions are true, return false
        return not (is_left or is_right or is_below or is_above)
