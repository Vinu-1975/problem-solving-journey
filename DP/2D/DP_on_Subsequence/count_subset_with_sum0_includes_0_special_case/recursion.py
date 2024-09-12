
""""
time complexity = O(2^n)
space complexity = O(n)

"""


class Solution:
	def perfectSum(self, arr, n, sum):
		# code here
        def dp(i,target):
            if i == 0:
                if(target == 0 and arr[0] == 0):
                    return 2
                if(target == 0 or target == arr[0]):
                    return 1
                return 0
            notPick = dp(i-1,target)
            pick = 0
            if(arr[i]<=target):
                pick = dp(i-1,target-arr[i])
            return notPick + pick
        
        return dp(n-1,sum)