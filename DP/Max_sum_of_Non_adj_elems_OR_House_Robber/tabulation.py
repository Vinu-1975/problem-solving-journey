
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
        for i in range(1,n):
            skip = dp[i-1]
            rob = nums[i]
            if i>1:
                rob += dp[i-2]
            dp[i] = max(skip,rob)
        
        return dp[n-1]