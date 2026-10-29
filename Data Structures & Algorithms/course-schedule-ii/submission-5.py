class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # course schedule, go through every courses and see
        # if we have a loop

        adj = collections.defaultdict(list)

        for u,v in prerequisites:
            adj[u].append(v)
        out = []

        visiting, visited = set(), set()

        def dfs(n):
            # already calculated
            if n in visited:
                return True
            
            # in path, loop found
            if n in visiting:
                return False
            
            visiting.add(n)
            
            for crs in adj[n]:
                if crs not in visited:
                    if not dfs(crs):
                        return False

            # else we are good
            visited.add(n)
            visiting.remove(n)
            out.append(n)

            return True
        
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return []

        return out


        