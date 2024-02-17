class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # time- O(nlogn)
        hashie = {}
        for n in nums:
            hashie[n] = hashie.get(n,0) + 1
        from heapq import heappush,heappop
        heapp = []
        for key,val in hashie.items():
            heappush(heapp,(val,key))
            if len(heapp) > k:
                heappop(heapp)
        return [it[1] for it in heapp]
