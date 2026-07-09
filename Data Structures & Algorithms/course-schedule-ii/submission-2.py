class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visiting, visited = set(), set()
        out = []

        adj = {i: [] for i in range(numCourses)}

        for u,v in prerequisites:
            adj[u].append(v)
        
        def dfs(course):
            if course in visiting:
                return False
            
            if course in visited:
                return True
            
            # add to current chain of course dependncies
            # to find possible cycles
            visiting.add(course)

            for dep in adj[course]:
                if not dfs(dep): return []
            
            # full dep cleared
            visited.add(course)
            visiting.remove(course)

            # add to output
            out.append(course)
            return True


        for i in range(numCourses):
            if not dfs(i): return []
        
        return out
        