# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ## Keep global variable for tracking max diameter/result
        ## diameter = max (left) + max(right) from a given node
        ## dfs will be used - but returns the height of each sub tree
        self.res = 0

        # returns height
        def dfs(curr):
            if not curr:
                return 0
            
            # get left height
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)

            # return back max height from given curr node
            return 1 + max(left, right)
        
        dfs(root)

        return self.res
        