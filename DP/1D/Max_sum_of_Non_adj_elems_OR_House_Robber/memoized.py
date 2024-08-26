
# for recursion:
    # time comeplexity = O(2^n) (2 is the choice to rob or skip)
    # space complexity = O(n)

# for memoized:
    # time comeplexity = O(n*2) ~ O(n)
    # space complexity = O(n)



class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {0:nums[0]}
        def dp(i):
            if i in memo:
                return memo[i]
            if i < 0:
                memo[i] = 0
                return memo[i]
            robThis = dp(i-2) + nums[i]
            skip = dp(i-1)
            memo[i] = max(robThis,skip)
            return memo[i]
        
        return dp(len(nums)-1)