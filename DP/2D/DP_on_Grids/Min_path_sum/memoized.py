class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n= len(grid), len(grid[0])
        memo = {}
        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == 0 and j == 0:
                memo[(i,j)] = grid[i][j]
                return memo[(i,j)]
            if i<0 or j<0:
                memo[(i,j)] = float('inf')
                return memo[(i,j)]
            top = grid[i][j] + dp(i-1,j)
            left = grid[i][j] + dp(i,j-1)
            memo[(i,j)] = min(top,left)
            return memo[(i,j)]

        return dp(m-1,n-1)