class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack(path)
                    path.pop()
        backtrack([])
        return res

        