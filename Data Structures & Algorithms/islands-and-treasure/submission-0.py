class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])

        def addRoom(r,c):
            # break conditions, invalid room
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == -1 or (r,c) in visit:
                return
            
            q.append([r,c])
            visit.add((r,c))
        
        # get valid gate locations and add to queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        
        # initial dist from gate
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist

                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)
            
            # update next layer distance
            dist += 1