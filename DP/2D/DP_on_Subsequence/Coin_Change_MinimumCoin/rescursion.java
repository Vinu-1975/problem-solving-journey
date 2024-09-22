class Solution {
    public int coinChange(int[] coins, int amount) {
        int res = dp(coins.length - 1,amount,coins);
        if (res >= (int) Math.pow(10,9)){
            return -1;
        }
        return res;
    }

    public int dp(int i,int amt,int[] coins){

        if (i == 0){
            if (amt % coins[0] == 0){
                return amt / coins[0];
            }else{
                return (int) Math.pow(10,9);
            }
        }

        int notTake = 0 + dp(i-1,amt,coins);
        int take = (int) Math.pow(10,9);
        if (coins[i] <= amt){
            take = 1 + dp(i,amt - coins[i],coins);
        }

        return Math.min(take,notTake);
    }
}