# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        q = collections.deque([root])
        res = []

        while q:
            qLen = len(q)
            # placeholder right node at every level]
            rightSide = None

            for i in range(qLen):
                node = q.popleft()

                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            
            # after each level, add rightmost to result
            if rightSide:
                res.append(rightSide.val)
        
        return res
        