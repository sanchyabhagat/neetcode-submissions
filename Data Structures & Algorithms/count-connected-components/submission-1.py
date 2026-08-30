class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # numOfUnconnected componetnes
        # 1. Run dfs for all nodes
        # 2. maintain visited
        # 3. Increment output for each layer completed via dfs

        out =  0
        visit = set()

        adj = collections.defaultdict(list)

        for node, edge in edges:
            adj[node].append(edge)
            adj[edge].append(node)
        
        def dfs(node):
            visit.add(node)
            for nei in adj[node]:
                if nei not in visit:

                    dfs(nei)
            
            return
        
        for node in range(n):
            if node not in visit:
                # visit.add(node)
                dfs(node)
                out += 1
            
            
        
        return out
        
        