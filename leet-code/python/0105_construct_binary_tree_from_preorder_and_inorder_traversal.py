# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    io_map = {val: index for index, val in enumerate(inorder)}
    
    def build(pos, poe, ios, ioe):
      if pos > poe:
        return None
      
      root = TreeNode(preorder[pos])
      
      ioi = io_map[root.val]
      left = ioi - ios
      
      root.left = build(pos + 1, pos + left, ios, ioi - 1)
      root.right = build(pos + left + 1, poe, ioi + 1, ioe)
      
      return root
      
    return build(0, len(preorder) - 1, 0, len(inorder) - 1)
      
      