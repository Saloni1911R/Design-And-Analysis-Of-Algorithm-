class Solution:

  def minimumPushes(self, word: str) -> int:
    n = len(word)
    res = 0
    for i in range(n):
      res += (i // 8 + 1)
    return res
