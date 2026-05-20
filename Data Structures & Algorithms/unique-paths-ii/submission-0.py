class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        # use one row and update in place
        dp = [0] * COLS
        # Target value always reachable so 1
        dp[COLS-1] = 1

        for r in reversed(range(ROWS)):
            for c in reversed(range(COLS)):
                # blocked
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                
                elif c < COLS-1:
                    # newColValue = bottomColValuePreviousCalculated + right
                    dp[c] = dp[c] + dp[c+1]

        return dp[0]
        
        