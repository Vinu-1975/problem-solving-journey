#User function Template for python3
class Solution:
    def minimizeCost(self, arr, k):
        # code here
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            if i == 0:
                memo[i] = 0
                return memo[i]
            res = [float('inf')] * k
            for j in range(1,k+1):
                if j<=i:
                    res[j-1] = dp(i-j) + abs(arr[i] - arr[i-j])
            memo[i] = min(res)
            return memo[i]
            
        
        return dp(len(arr)-1)