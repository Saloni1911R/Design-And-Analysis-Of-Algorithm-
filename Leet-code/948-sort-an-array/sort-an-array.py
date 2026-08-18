class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])

        return self.merging(left_half, right_half)

    def merging(self, A, B):
        merge = [0] * (len(A) + len(B))
        i, j, k = 0, 0, 0
        
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                merge[k] = A[i]
                i += 1
            else:
                merge[k] = B[j]
                j += 1
            k += 1
            
        while i < len(A):
            merge[k] = A[i]
            i += 1
            k += 1
            
        while j < len(B):
            merge[k] = B[j]
            j += 1
            k += 1
            
        return merge
