class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 1. Make sure graph is connected, visited ==n
        # 2. Make sure no cycles detected
        
        # Empty graph is tree
        if not n:
            return True
        
        visit = set()
        preMap = {c: [] for c in range(n)}

        for node, edge in edges:
            preMap[node].append(edge)
            preMap[edge].append(node)

        def dfs(node, prevNode):
            
            # if node == prevNode:
            #     return True
            if node in visit:
                return False
            visit.add(node)
            
            for edge in preMap[node]:
                if edge == prevNode:
                    continue
                if not dfs(edge, node): return False
            
            return True
        
        if dfs(0, -1) and len(visit) == n:
            return True

        return False
        