class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # idea is to keep dfsing from all points
        # maintaining a visited set so we dont duplicate our work
        # if a higher value is found we save it, and keep looking for more maximums
        # end condiiton is just visiting all n x n grid

        ROWS, COLS = len(grid), len(grid[0])

        visit = set()
        res = 0

        # todo
        def dfs(r, c):
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in visit or grid[r][c] == 0:
                return 0
            
            visit.add((r,c))
            
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)


        
        for r in range(ROWS):
            for c in range(COLS):
                    res = max(res, dfs(r,c))
        
        return res


        