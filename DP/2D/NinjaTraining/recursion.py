
"""

for recurison:
    time complexity = O(n^m) where m is the number of days and n is the number of activities
    space complexity = O(m) due to the recursive call stack.

"""


class Solution:
    def maximumPoints(self, arr, n):
        # Code here
        m, n = len(arr), len(arr[0])
        def dp(day,last): # last refers to the last performed activity
            if (day == 0):
                maxi = 0
                for i in range(n):
                    if (i!=last):
                        maxi = max(maxi,arr[day][i])
                return maxi
            maxi = 0
            for i in range(n):
                if (i!=last):
                    points = arr[day][i] + dp(day-1,i)
                    maxi = max(maxi,points)
            return maxi
        
        
        return dp(m-1,n) # n because it is a number that is out of index which indicate that no activity is performed
