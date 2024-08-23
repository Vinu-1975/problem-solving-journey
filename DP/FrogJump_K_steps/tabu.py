#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def minimizeCost(self, arr, k):
        # code here
        n = len(arr)
        dp = [0] * n
        dp[0] = 0
        for i in range(1,n):
            temp = [float('inf')]*k
            for j in range(k):
                if j<i:
                    temp[j] = dp[i-(j+1)] + abs(arr[i] - arr[i-(j+1)])
            dp[i] = min(temp)
        
        return dp[n-1]
                

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minimizeCost(arr,k)
        print(res)
        t -= 1


# } Driver Code Ends