
# for tabulation:
    # time comeplexity = O(n)
    # space = O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [-1] * (n)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,n):
            skip = dp[i-1]
            rob = 0
            if i-2 >= 0:
                rob = dp[i-2] + nums[i]
            dp[i] = max(skip,rob)
        
        return dp[n-1]