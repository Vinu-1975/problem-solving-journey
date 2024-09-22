class Solution {
    public int coinChange(int[] coins, int amount) {
        Map<String,Integer> memo = new HashMap<>();
        int res = dp(coins.length - 1,amount,coins,memo);
        if (res >= (int) Math.pow(10,9)){
            return -1;
        }
        return res;
    }

    public int dp(int i,int amt,int[] coins, Map<String,Integer> memo){
        String key = i + "-" + amt;
        if(memo.containsKey(key)){
            return memo.get(key);
        }
        if (i == 0){
            if (amt % coins[0] == 0){
                return amt / coins[0];
            }else{
                return (int) Math.pow(10,9);
            }
        }

        int notTake = 0 + dp(i-1,amt,coins,memo);
        int take = (int) Math.pow(10,9);
        if (coins[i] <= amt){
            take = 1 + dp(i,amt - coins[i],coins,memo);
        }
        
        int res = Math.min(take,notTake);
        memo.put(key,res);
        return res;
    }
}