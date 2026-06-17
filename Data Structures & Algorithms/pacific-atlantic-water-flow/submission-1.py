class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Question wording isnt great -> we want to see which cells can flow DOWN
        # to pacific ocean (left and top)
        # AND atlantic ocean -> Down and right 
        # break condition -> each cell away from sea should be greater than the prev
        # if prev > cur -> Skip this cell
        # we dfs from each side _> first and last row (pac and atl)
        # and dfs from left and right -> (pac and atl)
        # Final we have pac and atl sets
        # do intersection -> our result as list

        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, visit, prevHeight):
            if c not in range(COLS) or r not in range(ROWS) or (r,c) in visit or prevHeight> heights[r][c]:
                return
            visit.add((r,c))
            dfs(r+1, c, visit,heights[r][c])
            dfs(r-1, c, visit,heights[r][c])
            dfs(r, c+1, visit,heights[r][c])
            dfs(r, c-1, visit,heights[r][c])

            return
        
        for r in range(ROWS):
            #left and right sides
            dfs(r, 0, pac, 0)
            dfs(r, COLS-1, atl, 0)
        
        for c in range(COLS):
            # top and bottom sides
            dfs(0, c, pac, 0)
            dfs(ROWS-1, c, atl, 0)
        
        return list(pac.intersection(atl))
