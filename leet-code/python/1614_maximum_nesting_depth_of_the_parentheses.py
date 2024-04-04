class Solution:
  def maxDepth(self, s: str) -> int:
    max_depth = 0
    depth = 0
    for c in s:
      if c == "(":
        depth += 1
      elif c == ")":
        max_depth = max(max_depth, depth)
        depth -= 1
      
    return max_depth