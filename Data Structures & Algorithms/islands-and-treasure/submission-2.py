class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # find rooms with treasure first and add to queue
        # start bfs from all these points simultaneously
        # keep adding edit distance after each bfs layer (ie..e len fo queue)
        # make to skip[ duplicates vgia visit set and -1 for water for each room]

        q = deque()
        dist = 0

        rows, cols = len(grid), len(grid[0])
        visit = set()

        # helper to add neighbor rooms to queue
        def addRoom(r, c):
            if (r not in range(rows) or c not in range(cols) or (r,c) in visit or grid[r][c] == -1):
                return

            visit.add((r,c))
            q.append([r,c])
        
        # add initial 0s 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        
        while q:
            for i in range(len(q)):
                nr, nc = q.popleft()

                grid[nr][nc] = dist

                addRoom(nr-1,nc)
                addRoom(nr+1, nc)
                addRoom(nr,nc + 1)
                addRoom(nr,nc - 1)
            
            dist += 1

                
             
        