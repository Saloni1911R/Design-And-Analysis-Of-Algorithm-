class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        placeVal = 0
        placevalsix = -1
        temp = num
        while(temp > 0):
            remain = temp % 10
            if(remain == 6):
                 placevalsix = placeVal

            temp = temp//10
            placeVal += 1
        
        if(placevalsix == -1):
            return num
        
        return num + 3*(10**placevalsix)