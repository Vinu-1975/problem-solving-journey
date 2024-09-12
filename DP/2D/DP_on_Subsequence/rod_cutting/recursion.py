class Solution:
    def cutRod(self, price, n):
        #code here
        def dp(i,N):
            if i == 0:
                return N * price[0]
            notTake = 0 + dp(i-1,N)
            take = 0
            rod_length = i+1
            if rod_length <= N:
                take = price[i] + dp(i,N-rod_length)
            return max(notTake,take)
        
        return dp(n-1,n)

