class Solution {
    public int solve(int n, int m, int grid[][]) {
        // Code here
        int[][][] memo = new int[n][m][m];
        for (int[][] layer : memo) {
            for (int[] row : layer) {
                Arrays.fill(row, Integer.MIN_VALUE);
            }
        }
        int res = dp(0,0,m-1,grid,memo);
        return res;
    }
    
    private int dp(int i, int j1, int j2, int grid[][], int memo[][][]){
        int m = grid[0].length;
        int n = grid.length;
        if(j1<0 || j1>=m || j2<0 || j2>=m){
            return Integer.MIN_VALUE;
        }
        if (memo[i][j1][j2] != Integer.MIN_VALUE){
            return memo[i][j1][j2];
        }
        if(i == n-1){
            if(j1==j2){
                memo[i][j1][j2] = grid[i][j1];
            }else{
                memo[i][j1][j2] = grid[i][j1] + grid[i][j2];
            }
            return memo[i][j1][j2];
        }
        int maxi = Integer.MIN_VALUE;
        for(int dj1=-1;dj1<=1;dj1++){
            for(int dj2=-1;dj2<=1;dj2++){
                if(j1 == j2){
                    maxi = Math.max(maxi,grid[i][j1] + dp(i+1,j1+dj1,j2+dj2,grid,memo));
                }else{
                    maxi = Math.max(maxi,grid[i][j1] + grid[i][j2] + dp(i+1,j1+dj1,j2+dj2,grid,memo));
                }
            }
        }
        memo[i][j1][j2] = maxi;
        return memo[i][j1][j2];
    }
}