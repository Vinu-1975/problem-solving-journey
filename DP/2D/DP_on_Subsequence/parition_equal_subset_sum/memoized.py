class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        
        target = total_sum//2
        n = len(nums)

        def dp(i,target,memo):
            if(i,target) in memo:
                return memo[(i,target)]
            if target == 0:
                memo[(i,target)] = True
                return memo[(i,target)]
            if i == 0:
                if nums[0] == target:
                    memo[(i,target)] = True
                else:
                    memo[(i,target)] = False
                return memo[(i,target)]
            notTake = dp(i-1,target,memo)
            take = False
            if nums[i]<=target:
                take = dp(i-1,target-nums[i],memo)
            memo[(i,target)] = notTake or take
            return memo[(i,target)]


        res = dp(n-1,target,{})
        return res