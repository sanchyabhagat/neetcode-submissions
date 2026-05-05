class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {c: [] for c in range(numCourses)}

        for crs, pre in  prerequisites:
            preMap[crs].append(pre)

        visited, visiting = set(), set()
        output = []

        def dfs(crs):
            # cycle found
            if crs in visiting:
                return False
            
            # Already valid and visited
            if crs in visited:
                return True
            
            visiting.add(crs)

            # iterate through preReqs
            for c in preMap[crs]:
                if not dfs(c): return False
            
            visiting.remove(crs)
            
            # At this point this is valid
            visited.add(crs)
            output.append(crs)
            return True
        
        # loop through all options
        for crs in range(numCourses):
            if not dfs(crs): return []
        
        return output
        