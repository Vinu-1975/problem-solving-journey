class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if(n==0){
            return 0;
        }else if(n==1){
            return nums[0];
        }

        int excludeLast = dp(nums,0,n-2);
        int excludeFirst = dp(nums,1,n-1);

        return Math.max(excludeLast,excludeFirst);
    }

    private int dp(int[] nums, int start, int end){
        int n = end-start+1;

        if (n == 1) {
            return nums[start];
        }

        int[] dp_arr = new int[n];
        dp_arr[0] = nums[start];

        for(int i=1;i<n;i++){
            int notTake = dp_arr[i-1];
            int take = nums[start+i];
            if (i>=2){  // (i-2) >= 0
                take += dp_arr[i-2];
            }
            dp_arr[i] = Math.max(notTake,take);
        }

        return dp_arr[n-1];
    }
}