from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.

# def dp(i,W,wt,v,memo):
#     if (i,W) in memo:
#         return memo[(i,W)]
#     if i == 0:
#         if wt[0] <= W:
#             memo[(i,W)] = v[0]
#         else:
#             memo[(i,W)] = 0
#         return memo[(i,W)]
#     notTake = 0 + dp(i-1,W,wt,v,memo)
#     take = 0
#     if wt[i]<=W:
#         take = v[i] + dp(i-1,W-wt[i],wt,v,memo)
#     memo[(i,W)] = max(take,notTake)
#     return memo[(i,W)]


t = int(input())
for _ in range(t):
    n = int(input())
    wt = list(map(int,input().split()))[:n]
    v = list(map(int,input().split()))[:n]
    W = int(input())

    dp = [[0 for _ in range(W+1)] for _ in range(n)]

    for w in range(W+1):
        if wt[0] <= w:
            dp[0][w] = v[0]
    
    for i in range(1,n):
        for w in range(W+1):
            notTake = 0 + dp[i-1][w]
            take = 0
            if wt[i] <= w:
                take = v[i] + dp[i-1][w-wt[i]]
            dp[i][w] = max(take,notTake)
    
    print(dp[n-1][W])




