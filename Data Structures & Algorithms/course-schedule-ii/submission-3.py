class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        visited, visiting = set(), set()
        out = []

        adj = collections.defaultdict(list)

        for u,v in prerequisites:
            adj[u].append(v)
        
        def dfs(crs):
            if crs in visiting:
                return False

            if crs in visited:
                return True

            visiting.add(crs)

            for dep in adj[crs]:
                if dep not in visited:
                    if not dfs(dep): return False
            
            visiting.remove(crs)
            visited.add(crs)

            out.append(crs)

            return True
        
        
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return []
        
        if len(visited) == numCourses:
            return out
        
        return []

        
        