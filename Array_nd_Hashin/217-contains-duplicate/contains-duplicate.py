class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashie = {}
        for n in nums:
            hashie[n] = hashie.get(n,0)+1
            if hashie[n] >= 2:
                return True
        
        return False