class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        
        target = total_sum//2
        n = len(nums)
        def dp(i,target):
            if target == 0:
                return True
            if i == 0:
                if nums[0] == target:
                    return True
                else:
                    return False
            notTake = dp(i-1,target)
            take = False
            if nums[i]<=target:
                take = dp(i-1,target-nums[i])
            return notTake or take


        res = dp(n-1,target)
        return res