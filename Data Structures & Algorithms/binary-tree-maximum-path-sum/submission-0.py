# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root) -> int:
            # base case, 0 path sum
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # check for negative
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # potentially update result first
            # consider left and right split
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # return value WHITHOUT path split
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]

        