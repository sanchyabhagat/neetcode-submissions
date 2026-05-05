class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh, time = 0, 0
        q = deque()
        directions = [[0,1], [0,-1], [1, 0], [-1,0]]

        # get rotten locations and fresh counts
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1

                if grid[r][c] == 2:
                    q.append((r,c))
        
        while q and fresh > 0:
            # start at time = 0 and proceed with the rotting
            for i in range(len(q)):
                r,c = q.popleft()

                for dr,dc in directions:
                    row, col = r+dr, c+dc
                    # skip invalid cases and non fresh/empty cases
                    if row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] != 1:
                        continue
                    
                    grid[row][col] = 2
                    q.append((row,col))
                    fresh -= 1
                
            time += 1
        
        return time if fresh == 0 else -1


        