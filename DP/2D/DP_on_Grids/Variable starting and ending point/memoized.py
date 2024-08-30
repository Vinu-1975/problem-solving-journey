class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        def dp(i,j,memo):
            if (i,j) in memo:
                return memo[(i,j)]
            if j<0 or j>=n:
                memo[(i,j)] = float('inf')
                return memo[(i,j)]
            if i == 0:
                memo[(i,j)] = matrix[0][j]
                return memo[(i,j)]
            up = matrix[i][j] + dp(i-1,j,memo)
            leftDiag = matrix[i][j] + dp(i-1,j-1,memo)
            rightDiag = matrix[i][j] + dp(i-1,j+1,memo)
            memo[(i,j)] = min(up,leftDiag,rightDiag)
            return memo[(i,j)]
        
        res = float('inf')
        for j in range(n):
            memo = {}
            curr = dp(n-1,j,memo)
            res = min(res,curr)
        return res