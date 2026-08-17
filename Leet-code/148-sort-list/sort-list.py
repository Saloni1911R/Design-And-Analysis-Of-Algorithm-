# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Base case: if list is empty or has only one node
        if not head or not head.next:
            return head
        
        # Step 1: Split the list into two halves
        prev = None
        slow = head
        fast = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        # Disconnect the first half from the second half
        prev.next = None
        
        # Step 2: Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(slow)
        
        # Step 3: Merge the sorted halves
        return self.merge(left, right)
        
    def merge(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        # Attach the remaining nodes
        curr.next = l1 if l1 else l2
        return dummy.next
