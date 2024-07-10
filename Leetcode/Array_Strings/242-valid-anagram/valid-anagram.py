class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashie = {}

        for c in s:
            hashie[c] = hashie.get(c,0) + 1
        
        for c in t:
            if c in hashie:
                hashie[c] -= 1
            else:
                return False
        
        for v in hashie:
            if hashie[v] != 0:
                return False

        return True