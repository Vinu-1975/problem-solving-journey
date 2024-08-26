
"""

time complexity = O(n) * O(4) * O(3) = O(12n) ~ O(n)
space complexity = O(4) + O(4) = O(8) ~ O(1) 

"""


class Solution:
    def maximumPoints(self, arr, n):
        # Code here
        
        prev = [0 for _ in range(4)]
        
        prev[0] = max(arr[0][1],arr[0][2])
        prev[1] = max(arr[0][0],arr[0][2])
        prev[2] = max(arr[0][0],arr[0][1])
        prev[3] = max(arr[0][0],arr[0][1],arr[0][2])
        
        for day in range(1,n):
            temp = [0 for _ in range(4)]
            for last in range(4):
                temp[last] = 0
                for task in range(3):
                    if task!=last:
                        points = arr[day][task] + prev[task]
                        temp[last] = max(temp[last],points)
            prev = temp
        
        return prev[3]