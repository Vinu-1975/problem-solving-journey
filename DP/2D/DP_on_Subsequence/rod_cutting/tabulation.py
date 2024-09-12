class Solution:
    def cutRod(self, price, n):

        dp = [[0 for _ in range(n+1)] for _ in range(n)]
        
        for j in range(n+1):
            dp[0][j] = j * price[0]
        
        for i in range(1,n):
            for N in range(n+1):
                notTake = 0 + dp[i-1][N]
                take = 0
                rod_length = i+1
                if rod_length <= N:
                    take = price[i] + dp[i][N-rod_length]
                dp[i][N] = max(take,notTake)
        
        return dp[n-1][n]