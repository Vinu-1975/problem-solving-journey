class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        def dp(i,j):
            if j<0 or j>=n:
                return float('inf')
            if i == 0:
                return matrix[0][j]
            up = matrix[i][j] + dp(i-1,j)
            leftDiag = matrix[i][j] + dp(i-1,j-1)
            rightDiag = matrix[i][j] + dp(i-1,j+1)
            return min(up,leftDiag,rightDiag)
        
        res = float('inf')
        for j in range(n):
            curr = dp(n-1,j)
            res = min(res,curr)
        return res