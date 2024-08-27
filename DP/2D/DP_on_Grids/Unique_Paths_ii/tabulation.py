class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if m == 0 or n == 0:
            return 0

        if obstacleGrid[0][0] == 1:
            return 0
        
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                else:
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        top = dp[i-1][j]
                        left = dp[i][j-1]
                        dp[i][j] = top + left
        
        return dp[m-1][n-1]