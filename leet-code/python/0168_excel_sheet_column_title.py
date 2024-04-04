class Solution:
  def convertToTitle(self, columnNumber: int) -> str:
    res = ""
    
    while columnNumber > 0:
      loc = columnNumber % 26
      loc = 26 if loc == 0 else loc
      
      res = chr(loc + 64) + res
      columnNumber -= loc
      columnNumber //= 26

    return res
