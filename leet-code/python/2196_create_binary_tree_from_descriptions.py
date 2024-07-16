# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodeMap = defaultdict(TreeNode)
        hasParent = set()
        for d in descriptions:
            n = nodeMap[d[0]]
            n.val = d[0]
            c = nodeMap[d[1]]
            c.val = d[1]
            hasParent.add(c.val)

            if d[2]:
                n.left = c
            else:
                n.right = c
        
        for n in nodeMap:
            if n not in hasParent:
                return nodeMap[n]