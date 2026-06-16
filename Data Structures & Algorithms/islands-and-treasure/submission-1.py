class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # find treasure spots and add to queue and visit:
        # have a helper fucntion to addRoom to the queue - moving away from the treasure spots
        # each edit distance is 1 step away
        # so each iteration of the queue we increment distance
        # do this while q has elements

        q = deque()
        dist = 0
        visit = set() # make sure we dont double add a value for distance/treasures more than once
        ROWS, COLS = len(grid), len(grid[0])
        
        def addRoom(r,c):
            # -1 -> water BAD
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in visit or grid[r][c] == -1:
                return
            
            visit.add((r,c))
            q.append([r,c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visit.add((r,c))
                    q.append([r,c])
        
        while q:
            for i in range((len(q))):
                r,c = q.popleft()
                
                # set the current distance
                grid[r][c] = dist

                # traverse neighbors
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)
            
            dist += 1
        

        

