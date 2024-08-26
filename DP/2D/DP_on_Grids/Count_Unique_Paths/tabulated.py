class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for i in range(n)] for j in range(m)]

        dp[0][0] = 1

        for i in range(0,m):
            for j in range(0,n):
                if (i==0 and j==0):
                    continue
                else:
                    up = dp[i-1][j]
                    left = dp[i][j-1]
                    dp[i][j] = up + left
        
        return dp[m-1][n-1]