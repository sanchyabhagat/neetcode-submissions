class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # two things
        # 1. no cycle, we can use prevNode in the DFS to confirm we are not going backwards
        # 2. fully connected len(visit) == n

        visit = set()
        adj = collections.defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node, prevNode):
            if node in visit:
                return False
            
            visit.add(node)

            for nei in adj[node]:
                if nei == prevNode:
                    continue
                
                if not dfs(nei, node): return False
            
            return True
        
        # -1 is plakcehodler for prev node that doesnt exist
        if dfs(0, -1) and len(visit) == n:
            return True
        
        return False

        

        
        
        
        