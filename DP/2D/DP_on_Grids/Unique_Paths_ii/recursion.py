

"""

time complexity : O(2^(m+n)) (2 for top and left) (m+n for depth of recursion)
space complexity : O(m*n) (depth of recursion stack)

"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if m == 0 or n == 0:
            return 0
            
        if obstacleGrid[0][0] == 1:
            return 0

        def dp(i,j):
            if i == 0 and j == 0:
                return 1
            if i<0 or j<0:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            top = dp(i-1,j)
            left = dp(i,j-1)
            return top + left

        return dp(m-1,n-1)