class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    bigSize = 0
    char_index = [-1] * 128
    l = 0
    for r in range(len(s)):
      c = ord(s[r])
      if char_index[c] >= l:
        l = char_index[c] + 1
      
      char_index[c] = r
      
      bigSize = max(bigSize, r - l + 1)
    
    return bigSize
    