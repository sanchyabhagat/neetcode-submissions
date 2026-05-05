class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        output = 0

        adj = {c: [] for c in range(n)}

        for node, edge in edges:
            adj[node].append(edge)
            adj[edge].append(node)
        
        def dfs(node):
        
            for edge in adj[node]:
                if not edge in visit:
                    visit.add(edge)
                    dfs(edge)
            
            return
        
        for node in range(n):
            if node not in visit:
                visit.add(node)
                dfs(node)
                # at this point we get all connections to this node and becomes one entityt
                output += 1
        
        return output

        