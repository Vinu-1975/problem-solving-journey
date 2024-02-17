class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # time- O(nlogn)
        # space - O(n+k)
        # hashie = {}
        # for n in nums:
        #     hashie[n] = hashie.get(n,0) + 1
        # from heapq import heappush,heappop
        # heapp = []
        # for key,val in hashie.items():
        #     heappush(heapp,(val,key))
        #     if len(heapp) > k:
        #         heappop(heapp)
        # return [it[1] for it in heapp]

        #time - O(n)
        #space - O(n+k)
        hashie = {}
        for n in nums:
            hashie[n] = hashie.get(n,0) + 1
        
        buckets = [[] for _ in range(len(nums)+1)]

        for key,val in hashie.items():
            buckets[val].append(key)

        res = []

        for i in range(len(buckets)-1,-1,-1):
            if buckets[i]:
                res.extend(buckets[i])
            if len(res) > k:
                break
        
        return res[:k]



