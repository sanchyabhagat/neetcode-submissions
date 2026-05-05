# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ## recursive solution 1 liner
        #return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        ## Iterative DFS solution
        ## pre-order traversal  
        res = 1

        stack = [[root, 1]]
        while stack:
            node, curDepth = stack.pop()

            if node:
                res = max (res, curDepth)
                stack.append([node.left, 1 + curDepth])
                stack.append([node.right, 1 + curDepth])
        
        return res
