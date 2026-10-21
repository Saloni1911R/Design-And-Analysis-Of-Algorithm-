class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        l = len(flowerbed)
        if (n == 0):
            return True

        for i in range(l):
            if(flowerbed[i] == 0):
                leftbed = (i==0) or (flowerbed[i-1] == 0)
                rightbed = (i == l-1) or (flowerbed[i+1] == 0)
                if (leftbed & rightbed):
                    flowerbed[i] = 1
                    n -= 1
                    if (n == 0):
                        return True
        
        return False