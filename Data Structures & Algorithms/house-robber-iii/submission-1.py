# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # key things, return condition si node = null ->
        # return both with and return root values possible
        # at the end return the best results with or without original root

        def dfs(node):
            if not node:
                return [0,0]
            
            # get left maxs
            leftVals = dfs(node.left)

            rightVals = dfs(node.right)

            # option one take root and grandchildren NOT direct childs
            withRoot = node.val + leftVals[1] + rightVals[1]

            # eles eget best possible asnwer avaialble downstream for left or right, whether with oput without roots
            withoutRoot = max(leftVals) + max(rightVals)

            return [withRoot, withoutRoot]

        return max(dfs(root))
 

        