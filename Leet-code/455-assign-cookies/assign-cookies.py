class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        m = len(g)
        n = len(s)
        i = 0
        j = 0
        while(i < m and j < n):
            if(g[i] <= s[j]):
                i+=1
            j+=1
        
        return i
