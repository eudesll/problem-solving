class Solution:
  def isPalindrome(self, x: int) -> bool:
    xs = str(x)
    xsr = "" # xs[::-1]
    for c in xs:
      xsr = c + xsr
    
    return xs == xsr