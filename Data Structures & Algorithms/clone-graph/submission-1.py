"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # store the old -> new mappings in hashmap]
        # traverse each node via dfs
        # if already in hashmap -> return the copy
        # if not create it and traverse it's neighbors via dfs
        # finaly return the original copy
        oldToNew = {}

        def dfs(n):
            if n in oldToNew:
                return oldToNew[n]
            
            copy = Node(n.val)

            oldToNew[n] = copy

            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        
        return dfs(node) if node else None


        