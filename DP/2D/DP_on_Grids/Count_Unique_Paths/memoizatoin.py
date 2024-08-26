
"""

time complexity : O(m*n)
space complexity : O(m*n)

"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == 0 and j == 0:
                memo[(i,j)]= 1
                return memo[(i,j)]
            if i<0 or j<0:
                memo[(i,j)] = 0
                return memo[(i,j)]
            left = dp(i,j-1)
            top = dp(i-1,j)

            memo[(i,j)] = left+top
            return memo[(i,j)]

        return dp(m-1,n-1)

            