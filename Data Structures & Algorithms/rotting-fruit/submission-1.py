class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # find total NON-rotten that is the target
        # find rotten ones and add to a queue to preapre for bfs
        # perform bfs till we have valid banans to rot or if we hit target
        # Each ietration of we increase time -> minimize it

        target, time = 0,0
        q = collections.deque()

        ROWS, COLS = len(grid), len(grid[0])

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    target += 1
                
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        while q and target > 0:
            for i in range(len(q)):
                r,c = q.popleft()

                for dr, dc in dirs:
                    row = r + dr
                    col = c + dc

                    if row not in range(ROWS) or col not in range(COLS) or grid[row][col] != 1:
                        continue
            
                    grid[row][col] = 2
                    q.append((row,col))
                
                    target -= 1
            time += 1
        
        return time if target == 0 else -1



                
        