# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         # self.val = val
#         # self.next = next

class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        first_cp = -1
        prev_cp = -1
        min_dist = float('inf')
        
        # Maintain references to previous, current, and next nodes
        prev_node = head
        curr_node = head.next
        position = 2 # 1-indexed position of curr_node
        
        while curr_node.next:
            next_node = curr_node.next
            
            # Check for local maxima or local minima
            is_maxima = curr_node.val > prev_node.val and curr_node.val > next_node.val
            is_minima = curr_node.val < prev_node.val and curr_node.val < next_node.val
            
            if is_maxima or is_minima:
                if first_cp == -1:
                    first_cp = position
                else:
                    # Update minimum distance with adjacent critical point distance
                    min_dist = min(min_dist, position - prev_cp)
                
                # Update the most recent critical point position
                prev_cp = position
            
            # Move pointers forward
            prev_node = curr_node
            curr_node = next_node
            position += 1
            
        # If fewer than two critical points were found
        if first_cp == prev_cp:
            return [-1, -1]
            
        max_dist = prev_cp - first_cp
        return [min_dist, max_dist]
