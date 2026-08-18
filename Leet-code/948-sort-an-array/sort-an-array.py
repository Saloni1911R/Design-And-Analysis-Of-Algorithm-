class Solution(object):
    def sortArray(self, nums):
        n = len(nums)
        
        def down(size, i):
            while 2 * i + 1 < size:
                child = 2 * i + 1
                if child + 1 < size and nums[child+1] > nums[child]:
                    child += 1
                if nums[i] >= nums[child]: 
                    break
                nums[i], nums[child] = nums[child], nums[i]
                i = child

        for i in range(n // 2 - 1, -1, -1):
            down(n, i)
            
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            down(i, 0)
            
        return nums
