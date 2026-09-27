class Solution(object):
    def reverseParentheses(self, s):
        """ :type s: str :rtype: str """
        stack = []
        ans = []
        for c in s:
            if c == '(':
                stack.append(len(ans))
            elif c == ')':
                j = stack.pop()
                ans[j:] = ans[j:][::-1]
            else:
                ans.append(c)
        return ''.join(ans)