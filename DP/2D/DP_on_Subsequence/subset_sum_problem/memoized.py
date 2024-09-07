class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        memo = {}
        def dp(i,target):
            if(i,target) in memo:
                return memo[(i,target)]
            if target == 0:
                memo[(i,target)] = True
                return memo[(i,target)]
            if i == 0:
                memo[(i,target)] = arr[0] == target
                return memo[(i,target)]
            notTake = dp(i-1,target)
            take = False
            if target>=arr[i]:
                take = dp(i-1,target - arr[i])
            memo[(i,target)] =  take or notTake
            return memo[(i,target)]
        return dp(N-1,sum)
        
