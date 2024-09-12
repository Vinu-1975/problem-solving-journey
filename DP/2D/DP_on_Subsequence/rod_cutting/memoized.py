class Solution:
    def cutRod(self, price, n):
        #code here
        memo = {}
        def dp(i,N):
            if (i,N) in memo:
                return memo[(i,N)]
            if i == 0:
                memo[(i,N)] = N * price[0]
                return memo[(i,N)]
            notTake = 0 + dp(i-1,N)
            take = 0
            rod_length = i+1
            if rod_length <= N:
                take = price[i] + dp(i,N-rod_length)
            memo[(i,N)] = max(notTake,take)
            return memo[(i,N)]
        
        return dp(n-1,n)
