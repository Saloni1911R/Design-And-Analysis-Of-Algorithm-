from collections import defaultdict

class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :type rtype: int
        """
        # Map each row to a set of its reserved seats
        occupied = defaultdict(set)
        for row, seat in reservedSeats:
            occupied[row].add(seat)
            
        # Start by assuming every single row can fit 2 families
        max_groups = 2 * n
        
        # Process only the rows that have reservations
        for row, seats in occupied.items():
            # Check availability for the 3 valid blocks
            left = all(s not in seats for s in (2, 3, 4, 5))
            right = all(s not in seats for s in (6, 7, 8, 9))
            middle = all(s not in seats for s in (4, 5, 6, 7))
            
            # A completely empty row allows 2 groups (already added to max_groups)
            # We subtract from our initial assumption based on what is actually possible:
            if left and right:
                # Both sides are free -> can host 2 groups (no change needed)
                continue
            elif left or right or middle:
                # At least one block is free -> can host 1 group (subtract 1)
                max_groups -= 1
            else:
                # No blocks are free -> can host 0 groups (subtract 2)
                max_groups -= 2
                
        return max_groups

