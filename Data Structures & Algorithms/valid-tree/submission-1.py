class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # given size n of num of Nodes
        # we start at first node (0)
        # 1. Make sure no cycles -> trees have no cycle
        # 2. Fully connected -> we visited all nodes starting from first

        adj = {i: [] for i in range(n)}
        visit = set()

        for node, edge in edges:
            adj[node].append(edge)
            adj[edge].append(node)
        
        def dfs(node, prevNode):
            # check cycle
            if node in visit:
                return False
            
            # add it
            visit.add(node)
            
            # edges
            for edge in adj[node]:
                # make sure we dont go back - undirected
                if edge == prevNode:
                    continue
                
                if not dfs(edge, node): return False
            
            # means all is good till this node atleast
            return True
        

        if dfs(0, -1) and len(visit) == n:
            return True
        
        return False
        