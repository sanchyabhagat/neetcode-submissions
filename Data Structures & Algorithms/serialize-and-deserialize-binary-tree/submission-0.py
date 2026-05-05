# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    # use dfs, append "N" to result when terminal condition reached
    # do same for left and right subtrees recuversively.
    # return global variable result with "," delemiter
    # Preorder traversal -> root, left, right

    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            # terminal case
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)


        
    # Decodes your encoded data to tree.
    # make tree from given "," separated string
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        # global index of string of our tree ^
        self.i = 0

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
            
