class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # visit = set()
        n =  len(edges)
        adj = {c: [] for c in range(n+1)}

        def dfs(node, prevNode):
            if node in visit:
                return True
            
            visit.add(node)

            for nei in adj[node]:
                if nei == prevNode:
                    continue
                if dfs(nei, node): return True
            
            return False
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit = set()

            if dfs(u, -1):
                return [u, v]

        return []
            
        