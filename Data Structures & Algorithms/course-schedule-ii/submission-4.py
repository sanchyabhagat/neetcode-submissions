class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        visiting, visited = set(), set()
        res = []

        adj = collections.defaultdict(list)

        for u,v in prerequisites:
            adj[u].append(v)

        def dfs(course):
            if course in visiting:
                return False
            
            if course in visited:
                return True
            
            visiting.add(course)

            for nei in adj[course]:
                if nei not in visited:
                    if not dfs(nei):
                        return False
            
            visiting.remove(course)
            visited.add(course)
            res.append(course)

            return True

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return []
        
        if len(visited) == numCourses:
            return res
        
        return []

        
        