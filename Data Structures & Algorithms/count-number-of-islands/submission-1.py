class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # for each row and col, loop and find total isalnds
        # if up down left right is 1 add to visit and continue bfs
        # this was we visit all elemtns once that are connected
        # visit set to not repeat

        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        dirs = [[0,1], [0,-1], [1,0], [-1,0]] 

        def bfs(r, c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row,col = q.popleft()
                for dr, dc in dirs:
                    r, c = row+dr, col+dc
                    if (r in range(ROWS) and c in range(COLS) and ((r,c)) not in visit
                        and grid[r][c] == "1"):
                        q.append((r,c))
                        visit.add((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        
        return islands
        