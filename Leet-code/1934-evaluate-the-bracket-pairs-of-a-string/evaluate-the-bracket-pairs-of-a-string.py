class Solution(object):
    def evaluate(self, s, knowledge):
        """:type s: str

        :type knowledge: List[List[str]]
        :rtype: str
        """
        mapping = {k: v for k, v in knowledge}
        res = []
        i = 0
        n = len(s)

        while i < n:
          if s[i] == '(':
            i += 1
            key_start = i
            while i < n and s[i] != ')':
              i += 1
            key = s[key_start:i]
            res.append(mapping.get(key, '?'))
            i += 1  # skip closing bracket
          else:
            res.append(s[i])
            i += 1

        return ''.join(res)
