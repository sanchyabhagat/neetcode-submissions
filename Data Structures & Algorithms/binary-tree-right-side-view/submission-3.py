# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        out = []

        while q:
            # placeholder right node at every level
            rightSide = None
            for i in range(len(q)):
                node = q.popleft()

                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)

            # after each level, append right most to out
            if rightSide:
                out.append(rightSide.val)
        
        return out

        