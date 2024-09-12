from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.

def dp(i,W,w,v):
    if i == 0:
        if w[0] <= W:
            return v[0]
        else:
            return 0
    notTake = 0 + dp(i-1,W,w,v)
    take = 0
    if w[i]<=W:
        take = v[i] + dp(i-1,W-w[i],w,v)
    return max(take,notTake)


t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int,input().split()))[:n]
    w = list(map(int,input().split()))[:n]
    W = int(input())

    res = dp(n-1,W,w,v)
    print(res)



