class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visiting, visited = set(), set()
        out = []

        adj = {i : [] for i in range(numCourses)}

        for u,v in prerequisites:
            adj[u].append(v)
        
        def dfs(course):
            if course in visited:
                return True
            
            if course in visiting:
                return False
            
            visiting.add(course)

            for pre in adj[course]:
                if not dfs(pre):
                    return []
            
            visiting.remove(course)
            visited.add(course)
            out.append(course)

            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        
        return out
    