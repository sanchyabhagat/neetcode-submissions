# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # at each stage we return max with or without root
        # base case is node is null
        # at the end we can just decide and return teh max 
        def dfs(node):
            if not node:
                return [0,0]
            
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)

            withRoot = node.val + leftMax[1] + rightMax[1]

            withoutRoot = max(leftMax) + max(rightMax)

            return [withRoot, withoutRoot]
        
        return max(dfs(root))
        