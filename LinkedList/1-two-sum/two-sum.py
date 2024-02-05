class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashie = {}
        for i,n in enumerate(nums):
            difference = target - n
            if difference in hashie:
                return [hashie[difference],i]
            hashie[n] = i
        
        return []