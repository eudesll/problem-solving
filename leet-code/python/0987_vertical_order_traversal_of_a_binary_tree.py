# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = defaultdict(list)
        def dfs(node, x, y):
            if node == None:
                return
            
            nodes[y].append((node.val, x))

            dfs(node.left, x + 1, y - 1)
            dfs(node.right, x + 1, y + 1)
        
        dfs(root, 0, 0)

        res = []
        min_col = min(nodes.keys())
        for i in range(len(nodes)):
            sr = sorted(nodes[i + min_col], key=lambda n: (n[1], n[0]))
            mr = list(map(lambda n: n[0], sr))
            res.append(mr)

        return res