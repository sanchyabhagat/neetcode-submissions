# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, curMax):
            if not node:
                return 0
        
            res = 1 if node.val >= curMax else 0
            curMax = max(curMax, node.val)
            res += dfs(node.left, curMax)
            res += dfs(node.right, curMax)
            return res
        
        return dfs(root, root.val)

        
        