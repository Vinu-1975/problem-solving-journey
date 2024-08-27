class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])

        dp = [[float('inf') for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                else:
                    top = dp[i-1][j] + grid[i][j]
                    left = dp[i][j-1] + grid[i][j]
                    dp[i][j] = min(top,left)
        
        return dp[m-1][n-1]