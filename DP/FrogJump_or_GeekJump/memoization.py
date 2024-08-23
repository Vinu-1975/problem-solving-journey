class Solution:
    def minimumEnergy(self, height, n):
        memo = [-1] * n
        
        def dp(index):
            if memo[index] != -1:
                return memo[index]
            if index == 0:
                memo[index] = 0
                return memo[index]
            left = dp(index - 1) + abs(height[index] - height[index - 1])
            right = float('inf')
            if index > 1:
                right = dp(index - 2) + abs(height[index] - height[index - 2])
            memo[index] = min(left, right)
            return memo[index]
            
        return dp(n - 1)