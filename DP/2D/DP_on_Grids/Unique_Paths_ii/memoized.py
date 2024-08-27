class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if m == 0 or n == 0:
            return 0

        if obstacleGrid[0][0] == 1:
            return 0
        memo = {}
        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == 0 and j == 0:
                memo[(i,j)] = 1
                return memo[(i,j)]
            if i<0 or j<0:
                memo[(i,j)] = 0
                return memo[(i,j)]
            if obstacleGrid[i][j] == 1:
                memo[(i,j)] = 0
                return memo[(i,j)]
            top = dp(i-1,j)
            left = dp(i,j-1)
            memo[(i,j)] = top + left
            return memo[(i,j)]
        return dp(m-1,n-1)