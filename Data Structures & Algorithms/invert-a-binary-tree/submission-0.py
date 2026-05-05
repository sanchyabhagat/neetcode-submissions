# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if not root:
            return None
        
        # start inverting
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # invert left and right subtrees recursively
        self.invertTree(root.left)
        self.invertTree(root.right)

        # at this point we have inverted all subtrees
        return root
        