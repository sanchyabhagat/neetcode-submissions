# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        ## root -> take root or skip root
        ## if node == null. return 0, 0
        ## take root = root.val + children value without root (left adn right paths)
        ## skip root: direct children value with root

        def dfs(node):
            if not node:
                # since max sums will be zero
                # [withRoot, withoutRoot]
                return [0, 0]
            
            # get left path
            leftSums = dfs(node.left)
            # get right sums
            rightSums = dfs(node.right)

            # now we either pick or skip
            withRoot = node.val + leftSums[1] + rightSums[1]

            # we want max possible sums from each left and right options
            # which can be with our without the left/right roots
            withoutRoot = max(leftSums) + max(rightSums)

            return [withRoot, withoutRoot]
        
        withRoot, withoutRoot = dfs(root)

        return max(withRoot, withoutRoot)
        