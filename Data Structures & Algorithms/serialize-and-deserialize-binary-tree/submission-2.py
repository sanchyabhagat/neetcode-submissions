# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return

            # add the actual result    
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return
        
        dfs(root)

        return ",".join(res)
            

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # track index of the str globally
        self.i = 0
        vals = data.split(",")

        # recurse
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return
        
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()

            

        
