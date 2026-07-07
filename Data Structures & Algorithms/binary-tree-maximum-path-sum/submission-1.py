# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        res = [root.val] # using list as global var

        def dfs(node) -> int:
            if not node:
                return 0
            
            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)

            res[0] = max(res[0], node.val + leftMax + rightMax)

            # pick the better path to return
            return node.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]

        