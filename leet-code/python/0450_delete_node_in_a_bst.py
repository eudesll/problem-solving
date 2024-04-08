# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class Solution:
  def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root:
      return None
    
    if key > root.val:
      root.right = self.deleteNode(root.right, key)
    elif key < root.val:
      root.left = self.deleteNode(root.left, key)
    else:
      if not root.left and not root.right:
        return None
      
      if not root.left:
        child = root.right
        while child.left is not None:
          child = child.left
        
        root.val = child.val
        root.right = self.deleteNode(root.right, child.val)
      else:
        child = root.left
        while child.right is not None:
          child = child.right
        
        root.val = child.val
        root.left = self.deleteNode(root.left, child.val)
        
    return root