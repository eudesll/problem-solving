# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class Solution:
  def sumNumbers(self, root: Optional[TreeNode]) -> int:
    def sum(node, val):
      if node is None:
        return 0
      
      val = val * 10 + node.val
      return sum(node.left, val) + sum(node.right, val) or val
      
    return sum(root, 0)
        