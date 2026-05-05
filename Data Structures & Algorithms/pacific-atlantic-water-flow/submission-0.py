class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, visit, prevHeight):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or heights[r][c] < prevHeight:
                return
            
            visit.add((r,c))
            dfs(r-1, c, visit, heights[r][c])
            dfs(r+1, c, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pac, 0)
            dfs(ROWS-1, c, atl, 0)
        
        for r in range(ROWS):
            dfs(r, 0, pac, 0)
            dfs(r, COLS -1, atl, 0)
        
        return list(pac.intersection(atl))