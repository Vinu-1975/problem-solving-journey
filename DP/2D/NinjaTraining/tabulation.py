class Solution:
    def maximumPoints(self, arr, n):
        # Code here
        dp = [[0 for _ in range(4)] for _ in range(n)]
        
        dp[0][0] = max(arr[0][1],arr[0][2])
        dp[0][1] = max(arr[0][0],arr[0][2])
        dp[0][2] = max(arr[0][0],arr[0][1])
        dp[0][3] = max(arr[0][1],arr[0][2],arr[0][0])
        
        for day in range(1,n):
            for last in range(4):
                dp[day][last] = 0
                for activity in range(3):
                    if activity!=last:
                        points = arr[day][activity] + dp[day-1][activity]
                        dp[day][last] = max(dp[day][last],points)
        
        return dp[n-1][3]
