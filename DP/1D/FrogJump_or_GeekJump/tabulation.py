class Solution:
    def minimumEnergy(self, height, n):
        if n == 1:
            return 0  # If there's only one stair, no energy is required to stay on it
        
        dp = [0] * n
        
        dp[0] = 0
        dp[1] = abs(height[1] - height[0])
        
        for i in range(2, n):  # Start from i = 2 to avoid out-of-bounds errors
            jumpOnce = dp[i-1] + abs(height[i] - height[i-1])
            jumpTwice = dp[i-2] + abs(height[i] - height[i-2])
            dp[i] = min(jumpOnce, jumpTwice)
        
        return dp[-1]  # Return the energy required to reach the last stair

# Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        height = list(map(int, input().split()))
        ob = Solution()
        print(ob.minimumEnergy(height, n))
# Driver Code Ends
