class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        def dp(start,end,memo):
            if end in memo:
                return memo[end]
            if end == start:
                memo[end] = nums[start]
                return memo[end]
            elif end < start:
                memo[end] = 0
                return memo[end]
            take = nums[end] + dp(start,end-2,memo)
            notTake = dp(start,end-1,memo)
            memo[end] = max(take,notTake)
            return memo[end]
        
        return max(dp(1,n-1,{}),dp(0,n-2,{}))