# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = [root.val]

        def dfs(node):
            if not node:
                return 0
            
            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)

            res[0] = max(res[0], node.val + leftMax + rightMax)

            # at each path return the max of left or right, can only take one
            return node.val + max(leftMax, rightMax)

        
        dfs(root)

        return res[0]
        