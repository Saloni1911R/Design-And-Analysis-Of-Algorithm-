# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        # Base case: if the array section is empty, return None
        if not nums:
            return None
        
        # Find the middle index of the current array slice
        mid = len(nums) // 2
        
        # Create the root node with the middle element
        root = TreeNode(nums[mid])
        
        # Recursively build the left subtree using elements before the middle
        root.left = self.sortedArrayToBST(nums[:mid])
        
        # Recursively build the right subtree using elements after the middle
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root
