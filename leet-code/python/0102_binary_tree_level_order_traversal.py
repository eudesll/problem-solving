# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class Solution:
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    levels = []
    def getLevelNodes(node, level):
      if not node:
        return
      
      if len(levels) < level:
        levels.append([])
      
      levels[level - 1].append(node.val)
      getLevelNodes(node.left, level + 1)
      getLevelNodes(node.right, level + 1)
    
    getLevelNodes(root, 1)
    return levels
        