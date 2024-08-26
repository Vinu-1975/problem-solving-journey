"""

time complexity : O(2^(m+n))
space complexity : O(m+n)

"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def dp(i,j):
            if i == 0 and j == 0:
                return 1
            if i<0 or j<0:
                return 0
            left = dp(i,j-1)
            top = dp(i-1,j)

            return left+top

        return dp(m-1,n-1)

            