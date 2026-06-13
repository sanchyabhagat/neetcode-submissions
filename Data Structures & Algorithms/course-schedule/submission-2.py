class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # maintain visit set
        # dfs from each course with adj list
        # 
        visit = set()
        adj = {i : [] for i in range(numCourses)}

        for u,v in prerequisites:
            adj[u].append(v)
        
        def dfs(course):
            # circular dependency found
            if course in visit:
                return False
            
            # means we cleared all pre reqs already
            if adj[course] == []:
                return True
            
            visit.add(course)
            
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            # reset for new course path
            visit.remove(course)
            
            adj[course] = []

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True
                
                
            

