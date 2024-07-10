class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start,path,target):
            if target < 0:
                return
            if target == 0:
                res.append(path[:])
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                backtrack(i,path,target - candidates[i])
                path.pop()
        
        backtrack(0,[],target)
        return res