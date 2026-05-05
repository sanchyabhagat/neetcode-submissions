class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map course to preRequisites
        preMap = {i: [] for i in range(numCourses)}

        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        
        # maintain a visit set for each course
        visit = set()
        
        def dfs(crs):
            # if already visited, means we hit a cycle
            if crs in visit:
                return False
            
            # if no preReq, we hit another base case
            if preMap[crs] == []:
                return True
            
            visit.add(crs)

            # Check dependency for given course, see if cycle exists at any point
            for preReq in preMap[crs]:
                # immediately return False upstream
                if not dfs(preReq): return False
            visit.remove(crs)

            # remove preReq since we confirmed no dependency at this point
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        
        # If all possible courses have been traversed
        return True
        