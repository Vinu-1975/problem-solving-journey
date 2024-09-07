class Solution:
    def isSubsetSum(self, N, arr, sum):
        # Create a DP array initialized to False
        dp = [[False for _ in range(sum + 1)] for _ in range(N)]
        
        # There's always a subset with sum 0 which is the empty subset
        for i in range(N):
            dp[i][0] = True
        
        # Initialize the first row, we can only make a sum with the first element if it's <= sum
        if arr[0] <= sum:
            dp[0][arr[0]] = True
        
        # Fill the rest of dp table
        for i in range(1, N):
            for target in range(1, sum + 1):
                notTake = dp[i - 1][target]
                take = False
                if arr[i] <= target:
                    take = dp[i - 1][target - arr[i]]
                dp[i][target] = notTake or take
        
        # Return the value at the bottom-right corner of the dp table
        return dp[N - 1][sum]
