# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # global for resukt
        self.res = 0

        def dfs(node) -> int:
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            self.res = max(self.res, left + right)

            # we want the longer branch returned
            return 1 + max(left, right)
        
        dfs(root)
        return self.res
        