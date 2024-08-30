class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        def dp(i,j):
            if i == n-1:
                return triangle[n-1][j]
            down = triangle[i][j] + dp(i+1,j)
            diag = triangle[i][j] + dp(i+1,j+1)
            return min(down,diag)

        return dp(0,0)