class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # dfs to find first islands, mark these as 2
        # keep adding these to q
        # start bfs from queue at each level
        # if reaching other side - return current edit distance
        # if not, convert 0 -> 2 so we can move towards the second island

        q = deque()
        rows, cols = len(grid), len(grid[0])

        dirs = [[0,1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] != 1:
                return
            grid[r][c] = 2
            q.append((r,c))

            dfs(r-1, c)
            dfs(r+1,c)
            dfs(r, c+1)
            dfs(r, c-1)

        # mark the first isalnd as 2 and add to  q to start bfs
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r,c)
                    break
            if q: break
        
        # now start bfs from q
        dist = 0
        while q:
            # layer by layer
            for i in range(len(q)):
                r, c = q.popleft()

                # go through surroundings
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc

                    if nr in range(rows) and nc in range(cols):

                        if grid[nr][nc] == 1:
                            return dist
                
                        # convert to 2 by using bridging distance
                        elif grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            q.append((nr, nc))
            dist += 1
                    



        





        