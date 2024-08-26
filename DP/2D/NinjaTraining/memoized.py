
""""

for memoization:
    time complexity : O(m * n * n) where m is the number of days and n is the number of activities (extra n for loop inside recursion)
    space complexity : (m*n) includes the memoization table and the recursion call stack.
"""


class Solution:
    def maximumPoints(self, arr, n):
        # Code here
        m, n = len(arr), len(arr[0])
        memo = {}
        def dp(day,last): # last refers to the last performed activity
            if(day,last) in memo:
                return memo[(day,last)]
            if (day == 0):
                maxi = 0
                for i in range(n):
                    if (i!=last):
                        maxi = max(maxi,arr[day][i])
                memo[(day,last)] = maxi
                return memo[(day,last)]
            maxi = 0
            for i in range(n):
                if (i!=last):
                    points = arr[day][i] + dp(day-1,i)
                    maxi = max(maxi,points)
            memo[(day,last)] = maxi
            return memo[(day,last)]
        
        
        return dp(m-1,n) # n because it is a number that is out of index which indicate that no activity is performed
