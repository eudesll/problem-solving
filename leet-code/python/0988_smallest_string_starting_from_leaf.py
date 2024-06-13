from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class Solution:
  def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
    def small(node):
      if node.left is None and node.right is None:
        return [chr(node.val + 97)]

      opts = []
      if node.left:
        opts += small(node.left)
      if node.right:
        opts += small(node.right)
      
      return [o + chr(node.val + 97) for o in opts]
    
    all_options = small(root)
    return min(all_options)