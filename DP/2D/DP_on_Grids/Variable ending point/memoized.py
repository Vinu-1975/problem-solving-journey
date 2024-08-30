class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        memo = {}
        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == n-1:
                memo[(i,j)] = triangle[n-1][j]
                return memo[(i,j)]
            down = triangle[i][j] + dp(i+1,j)
            diag = triangle[i][j] + dp(i+1,j+1)
            memo[(i,j)] = min(down,diag)
            return memo[(i,j)]

        return dp(0,0)