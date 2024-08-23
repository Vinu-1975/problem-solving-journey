
"""

Time complexity : O(2^n) * n (2 is the choice to pick or not pick)
space complexity : O(2^n) * n 
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def f(i,arr):
            if i>=n:
                res.append(arr.copy())
                return
            arr.append(nums[i]) # pick
            f(i+1,arr)
            arr.pop() # not pick
            f(i+1,arr)
        
        f(0,[])
        return res