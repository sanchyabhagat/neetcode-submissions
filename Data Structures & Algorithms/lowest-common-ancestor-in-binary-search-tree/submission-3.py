# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # LCA here means where these two given nodes split off

        cur = root

        while cur:
            if cur.val > p.val and cur.val > q.val:
                cur = cur.left
            
            elif cur.val < p.val and cur.val < q.val:
                cur = cur.right
            
            else:
                return cur
        


        