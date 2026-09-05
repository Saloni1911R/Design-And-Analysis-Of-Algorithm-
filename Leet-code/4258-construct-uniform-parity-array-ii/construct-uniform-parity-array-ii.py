class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        # Find the minimum odd value in the array
        min_odd = float('inf')
        for x in nums1:
            if x % 2 == 1:
                if x < min_odd:
                    min_odd = x
        
        # If there are no odd numbers, the array is already uniformly even
        if min_odd == float('inf'):
            return True
            
        # If any even number is smaller than our smallest odd number, 
        # it cannot be transformed into an odd number.
        for x in nums1:
            if x % 2 == 0 and x < min_odd:
                return False
                
        return True
