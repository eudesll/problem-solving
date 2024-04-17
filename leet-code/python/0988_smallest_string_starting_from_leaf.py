from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class Solution:
  def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
    if root is None:
      return ""
    
    if root.left is None and root.right is None:
      return chr(root.val + 97)
    
    l = self.smallestFromLeaf(root.left)
    r = self.smallestFromLeaf(root.right)
    
    res = ""
    if l and r:
      res = l if l < r else r
    else:
      res = l if l else r
    
    return res + chr(root.val + 97)
  
  print("ababz" < "abz")