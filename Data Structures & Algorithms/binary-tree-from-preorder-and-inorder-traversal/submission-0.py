# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # easy lookup for indor value -> index map, which gives us the
        # size of left and right subtrees for a given root node
        indices = {val: idx for idx, val in enumerate(inorder)}

        # go pre order , root left and right 
        self.pre_idx = 0

        # go DFS recursively to make root -> left and right subtrees
        def dfs(l, r):
            # base case: left index needs to be less than right
            if l > r:
                return None
            
            # else proceed as normal
            # get cur root, rememeber preorder always gets us root value first guaranteed
            root_val = preorder[self.pre_idx]

            # increment for next root
            self.pre_idx += 1

            # make new treenode
            root = TreeNode(root_val)

            # get how many elements in left of this root
            # this info is from inorder traversal
            left_size = indices[root_val]

            # recurse for left subtree
            # we dont want this mid/already processed root included
            root.left = dfs(l, left_size-1)

            # recurse for right subtree
            # we dont want this mid/already processed root included
            root.right = dfs(left_size+1,r)
            
            return root
        
        return dfs(0, len(inorder)-1)

        