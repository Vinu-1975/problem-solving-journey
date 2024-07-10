class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O (N * log(M))
        hashie = collections.defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            hashie[sorted_word].append(word)
        
        return hashie.values()
