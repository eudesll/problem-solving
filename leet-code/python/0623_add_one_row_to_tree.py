# Definition for a binary tree node.
from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class Solution:
  def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
    def add(node, level):
      if node is None:
        return
      
      if level == depth - 1:
        node.left = TreeNode(val, node.left)
        node.right = TreeNode(val, None, node.right)
        return
      
      add(node.left, level + 1)
      add(node.right, level + 1)
    
    if depth == 1:
      root = TreeNode(val, root)
    else:
      add(root, 1)
        
    return root